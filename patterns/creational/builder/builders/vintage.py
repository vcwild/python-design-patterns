from typing import Any
from builders.builder import Builder
from products.vintage import VintageProduct


class VintageBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = VintageProduct()

    @property
    def product(self) -> VintageProduct:
        product = self._product
        self.reset()
        return product

    def produce_hat(self) -> None:
        self._product.add("vintage hat")

    def produce_pants(self) -> None:
        self._product.add("vintage pants")

    def produce_shirt(self) -> None:
        self._product.add("vintage shirt")

    def produce_shoes(self) -> None:
        self._product.add("vintage shoes")
