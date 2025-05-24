from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

RGB = Tuple[int, int, int]
CMYK = Tuple[int, int, int, int]


@dataclass(slots=True, frozen=True)
class Color:
    """Immutable colour swatch."""

    index: int
    name: str
    rgb: RGB
    cmyk: CMYK
    hex: str

    # ---- convenience --------------------------------------------------

    @classmethod
    def from_dict(cls, raw: Dict) -> "Color":
        return cls(
            index=raw["index"],
            name=raw["name"],
            rgb=tuple(raw["rgb"]),
            cmyk=tuple(raw["cmyk"]),
            hex=raw["hex"],
        )

    # nice default repr for debugging
    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.name}({self.index}, {self.hex})"


@dataclass(slots=True, frozen=True)
class ColorCombination(Sequence[Color]):
    """
    A reusable *container* for a palette entry.

    Behaves like an immutable list (`len()`,  index access, iteration),
    but also carries its `cid` and has a `.show()` helper that prints a
    rich preview (imported lazily so Rich stays an *optional* extra).
    """

    cid: int
    colors: Tuple[Color, ...]  # tuple for immutability

    # ---- sequence protocol -------------------------------------------

    def __getitem__(self, i: int) -> Color:  # type: ignore
        return self.colors[i]

    def __len__(self) -> int:
        return len(self.colors)

    # ---- helpers ------------------------------------------------------

    def hexes(self) -> List[str]:
        """Return `['#ffb2ef', '#ff4cc9', …]`."""
        return [c.hex for c in self.colors]

    def show(self, *, on_white: bool = True) -> None:  # pragma: no cover
        from .rich_view import show_combination

        show_combination(self, on_white=on_white)

    def __repr__(self) -> str:  # pragma: no cover
        return f"ColorCombination(cid={self.cid}, size={len(self)})"
