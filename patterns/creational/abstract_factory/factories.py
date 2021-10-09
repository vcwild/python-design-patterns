from abstract_factory import AbstractFactory
from abstract_objects import AbstractChair, AbstractTable
from objects import ModernChair, ModernTable, VintageChair, VintageTable


class ModernFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return ModernChair()

    def create_table(self) -> AbstractTable:
        return ModernTable()


class VintageFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return VintageChair()

    def create_table(self) -> AbstractTable:
        return VintageTable()
