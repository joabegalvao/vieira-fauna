#!/usr/bin/env python3
"""Gera as imagens otimizadas da landing page a partir dos arquivos originais.

Uso (na raiz do projeto):
    python3 tools/optimize-images.py

Requer Pillow (pip install pillow) e a pasta materiais-de-origem/. Os
originais nunca são alterados. Para trocar uma foto, substitua o arquivo de
origem ou edite a lista PHOTOS e rode o script novamente.

A imagem de compartilhamento (1200x630) é montada pelo Chromium, com as
fontes do site, por outro script:
    node tools/render-compartilhamento.js
"""
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "materiais-de-origem"
SRC = SOURCES / "fotos"
AVATAR_SRC = SOURCES / "avaliacoes"
LOGO_SRC = SOURCES / "logo" / "Logo Vieira.png"
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


# Azul do logo. O PNG recebido usa #004fd8, mais vivo que o azul da marca;
# a pedido do cliente, o azul é ajustado para #252f7d, o mesmo da página.
BLUE = (37, 47, 125)


def recolor_blue(logo: Image.Image) -> Image.Image:
    """Troca os pixels azuis do logo pela cor BLUE, mantendo a transparência
    (e, com ela, a suavização das bordas). Rosa e dourado não são tocados."""
    r, g, b, a = logo.split()
    # azul: b alto, r e g baixos
    mask_b = b.point(lambda v: 255 if v > 110 else 0)
    mask_r = r.point(lambda v: 255 if v < 110 else 0)
    mask_g = g.point(lambda v: 255 if v < 150 else 0)
    is_blue = ImageChops.multiply(ImageChops.multiply(mask_b, mask_r), mask_g)
    solid = Image.new("RGBA", logo.size, BLUE + (0,))
    solid.putalpha(a)
    return Image.composite(solid, logo, is_blue)


def build_logo() -> None:
    """O logo veio em PNG de 2172x724 px, com fundo transparente. O script só
    recorta a margem vazia e gera as larguras usadas na página."""
    logo = recolor_blue(Image.open(LOGO_SRC).convert("RGBA"))
    box = logo.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox()
    margin = 8
    mark = logo.crop((
        max(0, box[0] - margin), max(0, box[1] - margin),
        min(logo.width, box[2] + margin), min(logo.height, box[3] + margin),
    ))
    for width in (560, 280):
        out = resize_to_width(mark, width)
        out.save(OUT / f"logo-vieira-fauna-shopping-{width}.png", optimize=True)
        out.save(OUT / f"logo-vieira-fauna-shopping-{width}.webp", "WEBP", quality=92, method=6)
    print(f"logo-vieira-fauna-shopping: {mark.width}x{mark.height} (salvo em 560 e 280)")

    # Ícones: o logo inteiro fica ilegível em 32 px, então os ícones usam só o
    # "V" azul, recortado do próprio logo, sobre o fundo claro da página.
    v = logo.crop((90, 100, 585, 530))
    # o "i" encosta na haste direita do V: apaga o que fica à direita, abaixo do topo do V
    alpha = v.getchannel("A")
    alpha.paste(0, (500 - 90, 245 - 100, v.width, v.height))
    v.putalpha(alpha)
    v = v.crop(alpha.point(lambda a: 255 if a > 20 else 0).getbbox())
    for name, size in (("favicon-32", 32), ("apple-touch-icon", 180), ("icon-192", 192)):
        tile = Image.new("RGBA", (512, 512), (245, 239, 228, 255))  # fundo claro da página
        scale = 400 / max(v.width, v.height)
        fitted = v.resize((round(v.width * scale), round(v.height * scale)), Image.LANCZOS)
        tile.alpha_composite(fitted, ((512 - fitted.width) // 2, (512 - fitted.height) // 2))
        tile.convert("RGB").resize((size, size), Image.LANCZOS).save(OUT / f"{name}.png", optimize=True)
    print("ícones gerados a partir do V do logo")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_photos()
    build_avatars()
    build_logo()
    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"{len(list(OUT.iterdir()))} arquivos, {total / 1024:.0f} KB no total")
