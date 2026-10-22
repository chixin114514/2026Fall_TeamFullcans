#!/usr/bin/env python3
"""Preserve the user HEIC pair and decode it with macOS Quick Look.

``sips`` can produce black output for iPhone HDR gain-map HEIC files.  This
script intentionally uses ``qlmanage -t`` and records the decoded dimensions
and hashes for reproducibility.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LEFT = ROOT / "task2" / "results" / "IMG_5572.HEIC"
DEFAULT_RIGHT = ROOT / "task2" / "results" / "IMG_5573.HEIC"
DEFAULT_OUT = ROOT / "task2" / "data" / "user_capture"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def decode(source: Path, destination: Path, size: int) -> dict[str, object]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="quicklook-") as temp_name:
        temp_dir = Path(temp_name)
        subprocess.run(
            ["qlmanage", "-t", "-s", str(size), "-o", str(temp_dir), str(source)],
            check=True,
            capture_output=True,
            text=True,
        )
        generated = temp_dir / f"{source.name}.png"
        if not generated.is_file() or generated.stat().st_size == 0:
            raise RuntimeError(f"Quick Look 未生成有效 PNG: {source}")
        shutil.copy2(generated, destination)

    try:
        import cv2
        import numpy as np
    except ModuleNotFoundError as exc:
        raise RuntimeError(f"需要 OpenCV/NumPy 验证解码结果: {exc.name}") from exc
    image = cv2.imread(str(destination), cv2.IMREAD_COLOR)
    if image is None or image.size == 0 or int(np.count_nonzero(image)) == 0:
        raise RuntimeError(f"解码 PNG 无法被 OpenCV 读取或全黑: {destination}")
    return {
        "source": str(source),
        "source_sha256": sha256(source),
        "decoded": str(destination),
        "decoded_sha256": sha256(destination),
        "width": int(image.shape[1]),
        "height": int(image.shape[0]),
        "channels": int(image.shape[2]) if image.ndim == 3 else 1,
        "nonzero_pixels": int(np.count_nonzero(image)),
        "method": "macOS qlmanage -t Quick Look thumbnail",
        "quicklook_size": size,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", type=Path, default=DEFAULT_LEFT)
    parser.add_argument("--right", type=Path, default=DEFAULT_RIGHT)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--size", type=int, default=1600)
    args = parser.parse_args()
    records = [
        decode(args.left, args.out_dir / "decoded" / "left.png", args.size),
        decode(args.right, args.out_dir / "decoded" / "right.png", args.size),
    ]
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "decode_info.json").write_text(
        json.dumps({"records": records}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"records": records}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
