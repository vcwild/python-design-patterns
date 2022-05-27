

from abc import ABC, abstractmethod
from abstract import Component
from visitor import Visitor


class ComponentA(Component):
    def behave_a(self): ...

    def accept(self, visitor: Visitor):
        visitor.resolve_component_a(self)

class ComponentB(Component):
    def behave_b(self): ...

    def accept(self, visitor: Visitor):
        visitor.resolve_component_b(self)
