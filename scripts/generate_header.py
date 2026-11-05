"""Regenerate README ASCII cards: python scripts/generate_header.py [monospace-font.ttf].

Requires Pillow: python -m pip install Pillow==12.2.0
Pass a monospace font path on systems without Consolas or DejaVu Sans Mono.
"""
from pathlib import Path
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ART = ['██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗', '██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗', '██║   ██║██║██║        ██║   ██║   ██║██████╔╝', '╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗', ' ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║', '  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝', '██████╗  █████╗ ███╗   ██╗ ██████╗██╗  ██╗ ██████╗ ███╗   ██╗', '██╔══██╗██╔══██╗████╗  ██║██╔════╝██║  ██║██╔═══██╗████╗  ██║', '██████╔╝███████║██╔██╗ ██║██║     ███████║██║   ██║██╔██╗ ██║', '██╔══██╗██╔══██║██║╚██╗██║██║     ██╔══██║██║   ██║██║╚██╗██║', '██████╔╝██║  ██║██║ ╚████║╚██████╗██║  ██║╚██████╔╝██║ ╚████║', '╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝']
BG, PANEL, BORDER = "#091219", "#0e1d26", "#243c48"
CYAN, MINT, TEXT, MUTED = "#66d9ef", "#b0ef89", "#e3edf2", "#829aa6"
FONT_PATH = sys.argv[1] if len(sys.argv) > 1 else next(
    (p for p in ("C:/Windows/Fonts/consola.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")
     if Path(p).exists()), None)
if FONT_PATH is None:
    raise SystemExit("Pass the path to a monospace .ttf font as the first argument.")
font = ImageFont.truetype(FONT_PATH, 23)
small = ImageFont.truetype(FONT_PATH, 18)
assert len(ART) == 12, "Both names must retain all six ASCII rows"
assert max(font.getlength(line) for line in ART) < 964, "ASCII exceeds the canvas"


def frame(step):
    image = Image.new("RGB", (1060, 530), BG)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((16, 16, 1043, 513), radius=14, fill=PANEL, outline=BORDER, width=2)
    draw.line((17, 65, 1042, 65), fill=BORDER, width=1)
    draw.text((40, 31), "+  vxgm / profile", font=small, fill=TEXT)
    draw.text((780, 31), "ASCII TERMINAL / 01", font=small, fill=MUTED)
    for i, line in enumerate(ART):
        x = (1060 - font.getlength(line)) / 2
        y = 92 + i * 25 + (12 if i >= 6 else 0)
        draw.text((x, y), line, font=font, fill=BORDER)
        count = int(len(line) * min(1, step / 18))
        draw.text((x, y), line[:count], font=font, fill=CYAN if i < 6 else MINT)
    draw.line((48, 426, 1012, 426), fill=BORDER)
    command = "> design. build. simplify."
    count = int(len(command) * max(0, min(1, (step - 18) / 18)))
    draw.text((48, 448), command[:count], font=small, fill=MINT)
    if step < 36:
        draw.text((48 + small.getlength(command[:count]), 448), "_", font=small, fill=MINT)
    draw.text((48, 482), "CodiDevs / UI + Frontend", font=small, fill=TEXT)
    draw.text((726, 482), "Manta, Ecuador / VxGM", font=small, fill=MUTED)
    return image


ABOUT = [
    ("VICTOR BANCHÓN", CYAN),
    ("UI + Frontend / Fundador de CodiDevs", TEXT),
    ("Ing. en TI · ULEAM / Manta, Ecuador", MUTED),
    ("", TEXT),
    ("── lo que hago", MINT),
    ("Diseño interfaces. Construyo sistemas.", TEXT),
    ("Automatizo lo repetitivo.", TEXT),
    ("CRMs / portales / herramientas internas", MUTED),
    ("", TEXT),
    ("── mi proceso", MINT),
    ("entender > diseñar > construir > conectar", TEXT),
    ("Figma > React > Tailwind > Supabase > APIs", MUTED),
    ("", TEXT),
    ("── fuera del estudio", MINT),
    ("Hackatones: aprender qué NO construir.", TEXT),
    ("", TEXT),
    ("Menos Excel + WhatsApp. Más tiempo para crear.", CYAN),
]


def about_frame(step):
    image = Image.new("RGB", (900, 610), BG)
    draw = ImageDraw.Draw(image)
    columns = 60
    top = "┌─ ~/about ".ljust(columns - 1, "─") + "┐"
    bottom = "└" + " VxGM / EOF ──┘".rjust(columns - 1, "─")
    assert len(top) == len(bottom) == columns
    assert all(len(text) <= columns - 6 for text, _ in ABOUT)
    assert font.getlength(top) < 828, "About exceeds the canvas"
    x = (900 - font.getlength(top)) / 2
    draw.text((x, 22), top, font=font, fill=CYAN)
    for row in range(19):
        y = 50 + row * 27
        draw.text((x, y), "│" + " " * (columns - 2) + "│", font=font, fill=BORDER)
        if 1 <= row <= len(ABOUT):
            text, color = ABOUT[row - 1]
            count = int(len(text) * max(0, min(1, (step - (row - 1)) / 4)))
            draw.text((x + font.getlength("   "), y), text[:count], font=font, fill=color)
    draw.text((x, 563), bottom, font=font, fill=CYAN)
    return image


def save_card(name, frames, pause):
    static = ROOT / f"assets/{name}.png"
    animated = ROOT / f"assets/{name}.gif"
    frames[-1].save(static)
    frames[0].save(animated, save_all=True, append_images=frames[1:],
                   duration=[100] * (len(frames) - 1) + [pause], loop=0, optimize=True, disposal=1)
    with Image.open(animated) as gif:
        assert gif.is_animated and gif.n_frames > 1
        assert gif.size == frames[0].size
        assert gif.info["loop"] == 0
        gif.seek(gif.n_frames - 1)
        assert gif.convert("RGB").getbbox()
    assert animated.stat().st_size < 2_000_000, "Keep the profile lightweight"
    print(f"Generated {animated.name}: {animated.stat().st_size:,} bytes; static fallback OK")


if __name__ == "__main__":
    save_card("profile-ascii", [frame(step) for step in range(41)], 2600)
    save_card("about-ascii", [about_frame(step) for step in range(22)], 12000)
