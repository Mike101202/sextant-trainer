#!/usr/bin/env python3
"""Generate icon-192.png, icon-512.png and icon-512-maskable.png from icon.svg."""
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    raise SystemExit("Install Pillow first:  pip install pillow")

# Pillow can't render SVG. Use cairosvg if available, else require a PNG source.
try:
    import cairosvg
    cairosvg.svg2png(bytestring=Path("icon.svg").read_bytes(), write_to="icon-512.png", output_width=512, output_height=512)
except ImportError:
    raise SystemExit("Install cairosvg first:  pip install cairosvg")

for size in (192, 512):
    img = Image.open("icon-512.png").convert("RGBA").resize((size, size), Image.LANCZOS)
    img.save(f"icon-{size}.png")

# Maskable: add 10% padding so Android's launcher circle crop doesn't clip the mark.
src = Image.open("icon-512.png").convert("RGBA")
canvas = Image.new("RGBA", (512, 512), (18, 53, 91, 255))  # #12355b
inner = int(512 * 0.8)
canvas.paste(src.resize((inner, inner), Image.LANCZOS), ((512-inner)//2, (512-inner)//2), src)
canvas.save("icon-512-maskable.png")

print("Wrote icon-192.png, icon-512.png, icon-512-maskable.png")