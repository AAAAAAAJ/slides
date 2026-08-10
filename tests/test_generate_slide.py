from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "generate_slide.py"
SPEC = importlib.util.spec_from_file_location("generate_slide", MODULE_PATH)
assert SPEC and SPEC.loader
generate_slide = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generate_slide)


class GenerateSlideTests(unittest.TestCase):
    @patch.object(generate_slide, "_request_json")
    def test_submit_generation_uses_atlas_image_contract(self, request_json: Mock) -> None:
        request_json.return_value = {"code": 200, "data": {"id": "prediction-1"}}

        prediction_id = generate_slide.submit_generation(
            "test-key",
            "Minimal presentation slide",
            "google/nano-banana-2/text-to-image",
            "16:9",
            "2k",
        )

        self.assertEqual(prediction_id, "prediction-1")
        request_json.assert_called_once_with(
            "POST",
            "https://api.atlascloud.ai/api/v1/model/generateImage",
            "test-key",
            {
                "model": "google/nano-banana-2/text-to-image",
                "prompt": "Minimal presentation slide",
                "aspect_ratio": "16:9",
                "resolution": "2k",
                "output_format": "png",
            },
        )

    @patch.object(generate_slide, "_request_json")
    def test_wait_for_prediction_returns_first_output(self, request_json: Mock) -> None:
        request_json.side_effect = [
            {"code": 200, "data": {"status": "processing"}},
            {"code": 200, "data": {"status": "completed", "outputs": ["https://cdn.example/slide.png"]}},
        ]
        sleep = Mock()

        output_url = generate_slide.wait_for_prediction(
            "test-key",
            "prediction-1",
            timeout=30,
            poll_interval=0.01,
            sleep=sleep,
        )

        self.assertEqual(output_url, "https://cdn.example/slide.png")
        sleep.assert_called_once_with(0.01)

    @patch.object(generate_slide, "_request_json")
    def test_wait_for_prediction_reports_failure(self, request_json: Mock) -> None:
        request_json.return_value = {
            "code": 200,
            "data": {"status": "failed", "error": "invalid prompt"},
        }

        with self.assertRaisesRegex(generate_slide.AtlasCloudError, "invalid prompt"):
            generate_slide.wait_for_prediction("test-key", "prediction-1", 30, 0)

    @patch.object(generate_slide, "wait_for_prediction", return_value="https://cdn.example/slide.png")
    @patch.object(generate_slide, "submit_generation", return_value="prediction-1")
    @patch.object(generate_slide, "download_output")
    def test_generate_slide_runs_submit_poll_download(
        self,
        download: Mock,
        submit: Mock,
        wait: Mock,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "slide.png"
            prediction_id = generate_slide.generate_slide(
                "test-key",
                "prompt",
                output_path,
                timeout=12,
                poll_interval=0.5,
            )

        self.assertEqual(prediction_id, "prediction-1")
        submit.assert_called_once()
        wait.assert_called_once()
        download.assert_called_once_with("https://cdn.example/slide.png", output_path)

    def test_main_requires_api_key(self) -> None:
        with patch.dict("os.environ", {}, clear=True):
            self.assertEqual(generate_slide.main(["--prompt", "test"]), 2)


if __name__ == "__main__":
    unittest.main()
