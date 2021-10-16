from typing import Any
from builders.builder import Builder
from products.modern import ModernProduct


class ModernBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = ModernProduct()

    @property
    def product(self) -> ModernProduct:
        product = self._product
        self.reset()
        return product

    def produce_hat(self) -> None:
        self._product.add("modern hat")

    def produce_pants(self) -> None:
        self._product.add("modern pants")

    def produce_shirt(self) -> None:
        self._product.add("modern shirt")

    def produce_shoes(self) -> None:
        self._product.add("modern shoes")
