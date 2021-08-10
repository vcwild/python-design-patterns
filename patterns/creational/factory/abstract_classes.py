from abc import ABC, abstractclassmethod


class Creator(ABC):
    @abstractclassmethod
    def factory_method(self):
        ...

    def some_operation(self):
        product = self.factory_method()

        result = f"Creator has created {product}."

        return result


class Product(ABC):
    @abstractclassmethod
    def operation(self):
        ...
