from abc import ABC
from typing import Any


class Product(ABC):
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def get_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}\n")
