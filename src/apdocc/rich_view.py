from __future__ import annotations

from rich.console import Console
from rich.table import Table, box
from rich.text import Text

from .models import ColorCombination

CONSOLE = Console()


def show_combination(combo: ColorCombination, *, on_white: bool = True) -> None:
    tbl = Table(
        title=f"Combination {combo.cid}",
        show_header=False,
        pad_edge=False,
        expand=False,
        box=None,
    )
    for col in combo.colors:
        chip = "   "  # 3-space square
        tbl.add_row(
            f"[on {col.hex}]{chip}[/]",
            f"[bold]{col.name}[/] (#{col.index}, {col.hex})",
        )

    style = "on white" if on_white else ""
    CONSOLE.print(tbl, style=style)
    CONSOLE.print(Text(" ", style=style))  # spacer line
