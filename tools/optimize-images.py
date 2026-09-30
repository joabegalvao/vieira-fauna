#!/usr/bin/env python3
"""Gera as imagens otimizadas da landing page a partir dos arquivos originais.

Uso (na raiz do projeto):
    python3 tools/optimize-images.py

Requer Pillow (pip install pillow) e a pasta materiais-de-origem/. Os
originais nunca são alterados. Para trocar uma foto, substitua o arquivo de
origem ou edite a lista PHOTOS e rode o script novamente.

A marca (tools/marca/marca.svg) é desenhada por código. Antes de rodar este
script, gere o PNG da marca e a imagem de compartilhamento:
    node tools/marca/render-marca.js
Sem o PNG da marca, este script mantém os ícones que já estão em assets/img.
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "materiais-de-origem"
SRC = SOURCES / "fotos"
AVATAR_SRC = SOURCES / "avaliacoes"
MARK_PNG = ROOT / "tools" / "marca" / "marca-512.png"
OUT = ROOT / "assets" / "img"


# Nada é ampliado: a maior versão gerada é a do recorte original.
WIDTHS = (360, 540, 720)

# nome de saída -> (arquivo em materiais-de-origem/fotos, área usada ou None)
# A área é (esquerda, topo, direita, base) em pixels do original. As capturas
# trazem uma borda irregular de 2 a 3 px, que fica de fora.
PHOTOS = {
    "spitz-depois-do-banho": ("Screenshot 2026-09-30 101500.png", (3, 3, 889, 888)),
    "acara-bandeira": ("Screenshot 2026-09-30 101321.png", (3, 3, 499, 849)),
    "calopsita": ("Screenshot 2026-09-30 101228.png", (3, 3, 890, 890)),
    "aquario-plantado": ("Screenshot 2026-09-30 101400.png", (3, 3, 501, 846)),
    "decoracao-de-aquario": ("Screenshot 2026-09-30 101411.png", (3, 3, 885, 887)),
    "golden-fantasiado": ("Screenshot 2026-09-30 101519.png", (3, 3, 680, 844)),  # sem a seta do carrossel, à direita
    "tigre-dagua": ("Screenshot 2026-09-30 101546.png", (3, 3, 885, 889)),
}

# Fotos de perfil: nome de saída -> arquivo em materiais-de-origem/avaliacoes
AVATARS = {
    "avaliacao-larissa-franca": "Larissa Franca.png",
    "avaliacao-rafael-santos": "Rafael Santos.png",
    "avaliacao-gabriel-hr": "Gabriel HR.png",
}


def resize_to_width(im: Image.Image, width: int) -> Image.Image:
    if im.width <= width:
        return im.copy()
    height = round(im.height * width / im.width)
    return im.resize((width, height), Image.LANCZOS)


def save_set(im: Image.Image, name: str) -> None:
    for width in WIDTHS:
        if width < im.width:
            resize_to_width(im, width).save(
                OUT / f"{name}-{width}.webp", "WEBP", quality=82, method=6
            )
    im.save(OUT / f"{name}-{im.width}.webp", "WEBP", quality=82, method=6)
    # fallback JPEG para navegadores sem WebP
    im.save(OUT / f"{name}-{im.width}.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    print(f"{name}: {im.width}x{im.height}")


def build_photos() -> None:
    for name, (source, area) in PHOTOS.items():
        im = Image.open(SRC / source).convert("RGB")
        save_set(im.crop(area) if area else im, name)


def build_avatars() -> None:
    """Mantém o tamanho e a transparência originais (72x72 px)."""
    for name, source in AVATARS.items():
        im = Image.open(AVATAR_SRC / source).convert("RGBA")
        im.save(OUT / f"{name}.png", optimize=True)
        im.save(OUT / f"{name}.webp", "WEBP", quality=90, method=6)
        print(f"{name}: {im.width}x{im.height}")


def build_icons() -> None:
    """Favicon e ícones de atalho a partir da marca desenhada por código."""
    if not MARK_PNG.exists():
        print("marca-512.png não encontrado: ícones mantidos como estão")
        return
    mark = Image.open(MARK_PNG).convert("RGBA")
    for name, size in (("favicon-32", 32), ("apple-touch-icon", 180), ("icon-192", 192)):
        tile = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
        fitted = mark.resize((472, 472), Image.LANCZOS)
        tile.alpha_composite(fitted, (20, 20))
        if name == "apple-touch-icon":
            # o iOS não aceita transparência: fundo na cor da marca
            solid = Image.new("RGB", (512, 512), (18, 97, 92))
            solid.paste(tile, mask=tile.getchannel("A"))
            solid.resize((size, size), Image.LANCZOS).save(OUT / f"{name}.png", optimize=True)
        else:
            tile.resize((size, size), Image.LANCZOS).save(OUT / f"{name}.png", optimize=True)
    print("ícones gerados a partir da marca")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_photos()
    build_avatars()
    build_icons()
    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"{len(list(OUT.iterdir()))} arquivos, {total / 1024:.0f} KB no total")
