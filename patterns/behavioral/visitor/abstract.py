from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def accept(self, visitor): ...

class Visitor(ABC):
    @abstractmethod
    def resolve_component_a(self, element: Component): ...

    @abstractmethod
    def resolve_component_b(self, element: Component): ...
