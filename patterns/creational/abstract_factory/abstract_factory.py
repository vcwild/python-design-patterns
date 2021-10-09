from abc import ABC, abstractmethod
from abstract_objects import AbstractChair, AbstractTable


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        ...

    @abstractmethod
    def create_table(self) -> AbstractTable:
        ...
