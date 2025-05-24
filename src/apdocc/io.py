from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from .models import Color, ColorCombination


def load_palette(path: str | Path) -> Dict[int, Color]:
    raw = json.loads(Path(path).read_text())
    return {c["index"]: Color.from_dict(c) for c in raw}


def load_combinations(
    path: str | Path, palette: Dict[int, Color]
) -> Dict[int, ColorCombination]:
    raw = json.loads(Path(path).read_text())
    combos: Dict[int, ColorCombination] = {}
    for k, indices in raw.items():
        combos[int(k)] = ColorCombination(
            cid=int(k),
            colors=tuple(palette[i] for i in indices if i in palette),
        )
    return combos
