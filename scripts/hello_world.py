#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "rich",
# ]
# ///
# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false

from rich import print


def main():
    print("Run via `uv run scripts/hello_world.py`")
    print("Or `chmod +x scripts/hello_world.py` and `./scripts/hello_world.py`")


if __name__ == "__main__":
    main()
