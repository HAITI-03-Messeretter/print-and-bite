"""Logo in einer Theme-Farbe exportieren.

Das Logo liegt freigestellt (transparenter Hintergrund) in assets/img/logo-*.png.
Dieses Skript färbt alle vier Teile (full, wordmark, printer, subtitle) in einer Farbe ein
und legt sie unter assets/logo/<name>-<teil>.png ab.

    python tools/logo-einfaerben.py m2 "#4a1f2c"

Benötigt Pillow (pip install pillow).
"""

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PARTS = ["full", "wordmark", "printer", "subtitle"]


def recolor(source: Path, target: Path, hex_color: str) -> None:
    rgb = tuple(int(hex_color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
    alpha = Image.open(source).convert("RGBA").getchannel("A")
    out = Image.new("RGBA", alpha.size, (*rgb, 0))
    out.putalpha(alpha)
    target.parent.mkdir(parents=True, exist_ok=True)
    out.save(target, optimize=True)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    name, hex_color = sys.argv[1], sys.argv[2]
    for part in PARTS:
        target = ROOT / "assets" / "logo" / f"{name}-{part}.png"
        recolor(ROOT / "assets" / "img" / f"logo-{part}.png", target, hex_color)
        print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
