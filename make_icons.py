#!/usr/bin/env python3
"""Generate icon-192.png, icon-512.png and icon-512-maskable.png from icon.svg."""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("Install Pillow first:  pip install pillow")

try:
    import cairosvg
except ImportError:
    raise SystemExit("Install cairosvg first:  pip install cairosvg")

# Render the SVG to a 512x512 master PNG.
cairosvg.svg2png(
    bytestring=Path("icon.svg").read_bytes(),
    write_to="icon-512.png",
    output_width=512,
    output_height=512,
)

master = Image.open("icon-512.png").convert("RGBA")
master.save("icon-512.png")
master.resize((192, 192), Image.LANCZOS).save("icon-192.png")

# Maskable: 80% design centred on a solid-blue 512x512 canvas so Android's
# circular launcher crop doesn't clip the mark.
inner = int(512 * 0.8)
small = master.resize((inner, inner), Image.LANCZOS)
canvas = Image.new("RGBA", (512, 512), (18, 53, 91, 255))
pos = ((512 - inner) // 2, (512 - inner) // 2)
canvas.paste(small, pos, small)  # FIXED: source and mask are the same size
canvas.save("icon-512-maskable.png")

print("Wrote icon-192.png, icon-512.png, icon-512-maskable.png")
