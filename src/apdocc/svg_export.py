#!/usr/bin/env python3
# ──────────────────────────────────────────────────────────────────────
#  Generate docs/combos.svg
#  • "Combination <cid>:" prefix  • colour chips  • fixed-width name col • hex list
#  • rows sorted by (#-of-colours, cid)
# ──────────────────────────────────────────────────────────────────────
from __future__ import annotations

from math import ceil
from pathlib import Path
from textwrap import dedent

from apdocc import ColorCombination, load_combinations, load_palette

# ─────────────────────────  visual constants  ─────────────────────────
TILE = 24  # chip size (px)
GAP = 8  # gap between major chunks
ROW_PAD = 6
FONT = "sans-serif"
FONT_SIZE = 12
AVG_CHAR = FONT_SIZE * 0.60  # crude average px width


# ─────────────────────────  geometry helpers  ─────────────────────────
def _prefix_width(combos: list[ColorCombination]) -> int:
    """Pixel width for the longest 'Combination nnn:' prefix."""
    longest = max(len(f"Combination {c.cid}:") for c in combos)
    return ceil(longest * AVG_CHAR) + GAP * 2


def _names_col_width(combos: list[ColorCombination]) -> int:
    """Pixel width for the longest 'idx name, …' string."""
    longest = max(
        len(", ".join(f"{col.index} {col.name}" for col in combo))
        for combo in combos
    )
    return ceil(longest * AVG_CHAR) + GAP * 2


# ────────────────────────  per-row renderer  ──────────────────────────
def _row_svg(
    y: int,
    combo: ColorCombination,
    prefix_x: int,
    chip_x: int,
    names_x: int,
    names_w: int,
) -> str:
    parts: list[str] = []

    # 0️⃣  prefix  -------------------------------------------------------
    prefix = f"Combination {combo.cid}:"
    parts.append(
        f'<text x="{prefix_x}" y="{y + TILE/2}" '
        f'font-weight="bold" dominant-baseline="middle">{prefix}</text>'
    )

    # 1️⃣  chips  --------------------------------------------------------
    x = chip_x
    for col in combo:
        parts.append(
            f'<rect x="{x}" y="{y}" width="{TILE}" height="{TILE}" '
            f'fill="{col.hex}" stroke="black" stroke-width="0.5"/>'
        )
        x += TILE + GAP

    # 2️⃣  names column  -------------------------------------------------
    names_txt = ", ".join(f"{c.index} {c.name}" for c in combo)
    parts.append(
        f'<text x="{names_x}" y="{y + TILE/2}" '
        f'dominant-baseline="middle">{names_txt}</text>'
    )

    # 3️⃣  hex list  -----------------------------------------------------
    hexes_x = names_x + names_w
    hexes = "[" + ", ".join(c.hex for c in combo) + "]"
    parts.append(
        f'<text x="{hexes_x}" y="{y + TILE/2}" '
        f'font-family="monospace" dominant-baseline="middle">{hexes}</text>'
    )

    return "\n".join(parts)


# ─────────────────────────  main exporter  ────────────────────────────
def export_svg(
    colors_file: str = "src/apdocc/colors.json",
    combos_file: str = "src/apdocc/combinations.json",
    out_file: str = "docs/combos.svg",
) -> Path:
    """Generate *docs/combos.svg* and return its Path."""
    palette = load_palette(colors_file)
    combos = load_combinations(combos_file, palette)

    rows: list[ColorCombination] = sorted(
        combos.values(), key=lambda c: (len(c), c.cid)
    )

    max_tiles = max(len(r) for r in rows)
    prefix_w = _prefix_width(rows)
    names_w = _names_col_width(rows)

    # horizontal anchors
    prefix_x = ROW_PAD
    chip_x = prefix_x + prefix_w
    chip_strip_w = max_tiles * (TILE + GAP)
    names_x = chip_x + chip_strip_w + GAP * 2

    # svg canvas
    row_h = TILE + ROW_PAD * 2
    width = names_x + names_w + 450  # space for hex column
    height = len(rows) * row_h

    svg = [
        dedent(
            f"""\
            <svg xmlns="http://www.w3.org/2000/svg"
                 width="{width}" height="{height}"
                 font-family="{FONT}" font-size="{FONT_SIZE}px">
            """
        )
    ]

    for i, combo in enumerate(rows):
        y = i * row_h + ROW_PAD
        svg.append(
            _row_svg(
                y,
                combo,
                prefix_x=prefix_x,
                chip_x=chip_x,
                names_x=names_x,
                names_w=names_w,
            )
        )

    svg.append("</svg>")

    out = Path(out_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(svg), encoding="utf-8")
    print(f"wrote {out}  ({out.stat().st_size/1024:.1f} kB)")
    return out


# ────────────────────────────  CLI hook  ──────────────────────────────
if __name__ == "__main__":
    export_svg()
