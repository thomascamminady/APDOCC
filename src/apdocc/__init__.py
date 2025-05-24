from .io import load_combinations, load_palette
from .models import Color, ColorCombination

Colors = load_palette("src/apdocc/colors.json")
Combinations = load_combinations("src/apdocc/combinations.json", Colors)

__all__ = [
    "Color",
    "ColorCombination",
    "Colors",
    "Combinations",
]
