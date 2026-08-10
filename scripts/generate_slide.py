#!/usr/bin/env python3
"""Generate a slide image from a style prompt using Atlas Cloud."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_API_BASE = "https://api.atlascloud.ai"
DEFAULT_MODEL = "google/nano-banana-2/text-to-image"
SUCCESS_STATUSES = {"completed", "succeeded"}
FAILURE_STATUSES = {"failed", "canceled", "cancelled"}


class AtlasCloudError(RuntimeError):
    """Raised when Atlas Cloud cannot complete an image generation request."""


def _request_json(
    method: str,
    url: str,
    api_key: str,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "style-prompt-studio/1.0",
        },
    )
    try:
        with urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise AtlasCloudError(f"Atlas Cloud returned HTTP {exc.code}: {detail}") from exc
    except (URLError, TimeoutError) as exc:
        raise AtlasCloudError(f"Atlas Cloud request failed: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise AtlasCloudError("Atlas Cloud returned invalid JSON") from exc

    if not isinstance(result, dict):
        raise AtlasCloudError("Atlas Cloud returned an unexpected response")
    code = result.get("code")
    if code not in (None, 0, 200):
        raise AtlasCloudError(str(result.get("message") or result.get("msg") or result))
    return result


def _prediction_data(response: dict[str, Any]) -> dict[str, Any]:
    data = response.get("data", response)
    if not isinstance(data, dict):
        raise AtlasCloudError("Atlas Cloud response is missing prediction data")
    return data


def submit_generation(
    api_key: str,
    prompt: str,
    model: str,
    aspect_ratio: str,
    resolution: str,
    api_base: str = DEFAULT_API_BASE,
) -> str:
    response = _request_json(
        "POST",
        f"{api_base.rstrip('/')}/api/v1/model/generateImage",
        api_key,
        {
            "model": model,
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
            "output_format": "png",
        },
    )
    prediction_id = _prediction_data(response).get("id")
    if not prediction_id:
        raise AtlasCloudError("Atlas Cloud response is missing a prediction ID")
    return str(prediction_id)


def wait_for_prediction(
    api_key: str,
    prediction_id: str,
    timeout: float,
    poll_interval: float,
    api_base: str = DEFAULT_API_BASE,
    sleep: Callable[[float], None] = time.sleep,
) -> str:
    deadline = time.monotonic() + timeout
    url = f"{api_base.rstrip('/')}/api/v1/model/prediction/{prediction_id}"
    while time.monotonic() < deadline:
        data = _prediction_data(_request_json("GET", url, api_key))
        status = str(data.get("status", "")).lower()
        if status in SUCCESS_STATUSES:
            outputs = data.get("outputs") or []
            if not outputs:
                raise AtlasCloudError("Atlas Cloud completed without an output URL")
            return str(outputs[0])
        if status in FAILURE_STATUSES:
            detail = data.get("error") or data.get("message") or "unknown error"
            raise AtlasCloudError(f"Atlas Cloud generation failed: {detail}")
        sleep(poll_interval)
    raise AtlasCloudError(f"Atlas Cloud generation timed out after {timeout:g} seconds")


def download_output(url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urlopen(url, timeout=120) as response:
            content = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise AtlasCloudError(f"Could not download generated slide: {exc}") from exc
    if not content:
        raise AtlasCloudError("Generated slide download was empty")
    output_path.write_bytes(content)


def generate_slide(
    api_key: str,
    prompt: str,
    output_path: Path,
    model: str = DEFAULT_MODEL,
    aspect_ratio: str = "16:9",
    resolution: str = "2k",
    timeout: float = 300,
    poll_interval: float = 3,
    api_base: str = DEFAULT_API_BASE,
) -> str:
    prediction_id = submit_generation(api_key, prompt, model, aspect_ratio, resolution, api_base)
    output_url = wait_for_prediction(
        api_key,
        prediction_id,
        timeout,
        poll_interval,
        api_base,
    )
    download_output(output_url, output_path)
    return prediction_id


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", required=True, help="Slide prompt, for example one copied from PROMPTS.md")
    parser.add_argument("--output", type=Path, default=Path("slide.png"), help="Output image path")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Atlas Cloud image model ID")
    parser.add_argument("--aspect-ratio", default="16:9", help="Generated image aspect ratio")
    parser.add_argument("--resolution", choices=("1k", "2k", "4k"), default="2k")
    parser.add_argument("--timeout", type=float, default=300, help="Maximum polling time in seconds")
    parser.add_argument("--poll-interval", type=float, default=3, help="Polling interval in seconds")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    api_key = os.getenv("ATLASCLOUD_API_KEY", "").strip()
    if not api_key:
        print("ATLASCLOUD_API_KEY is required", file=sys.stderr)
        return 2
    try:
        prediction_id = generate_slide(
            api_key=api_key,
            prompt=args.prompt,
            output_path=args.output,
            model=args.model,
            aspect_ratio=args.aspect_ratio,
            resolution=args.resolution,
            timeout=args.timeout,
            poll_interval=args.poll_interval,
        )
    except AtlasCloudError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Generated {args.output} (prediction {prediction_id})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
