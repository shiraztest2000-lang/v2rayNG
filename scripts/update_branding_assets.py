#!/usr/bin/env python3
"""Regenerate SHZv2rayNG app/store icon assets from the canonical branding logo."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
LOGO = ROOT / "branding" / "SHZv2rayNG-logo.png"
APP = ROOT / "V2rayNG" / "app" / "src" / "main"
STORE_ICON = ROOT / "fastlane" / "metadata" / "android" / "en-US" / "images" / "icon.png"
if not LOGO.is_file():
    raise SystemExit(f"Canonical logo not found: {LOGO}")
with Image.open(LOGO) as source:
    logo = source.convert("RGBA")

targets = [APP / "ic_launcher-web.png", STORE_ICON]
for folder in (APP / "res").glob("mipmap-*"):
    if folder.is_dir():
        for name in ("ic_launcher.png", "ic_launcher_foreground.png",
                     "ic_launcher_round.png", "ic_banner.png",
                     "ic_banner_foreground.png"):
            candidate = folder / name
            if candidate.is_file():
                targets.append(candidate)

updated = []
for path in sorted(set(targets)):
    if not path.is_file():
        continue
    with Image.open(path) as old:
        width, height = old.size
    margin = 0.78 if "foreground" in path.name else 0.88
    fitted = logo.copy()
    fitted.thumbnail((max(1, int(width * margin)), max(1, int(height * margin))),
                     Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    canvas.alpha_composite(fitted, ((width - fitted.width) // 2,
                                    (height - fitted.height) // 2))
    canvas.save(path, format="PNG", optimize=True)
    with Image.open(path) as check:
        if check.size != (width, height):
            raise SystemExit(f"Dimension changed unexpectedly: {path}")
    updated.append(f"{path.relative_to(ROOT)} ({width}x{height})")
if not updated:
    raise SystemExit("No branding assets were updated.")
print("Updated SHZv2rayNG branding assets:\n" + "\n".join(updated))

# Trigger the automated dual-branch branding and release workflow.
