from typing import Any
from interface import Component


class Leaf(Component):
    def __init__(self) -> None:
        self.name = "leaf"

    def __repr__(self) -> str:
        return f"Leaf(name={self.name})"

    def execute(self) -> Any:
        return 1
