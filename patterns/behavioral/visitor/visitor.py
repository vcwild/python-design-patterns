from abc import ABC, abstractmethod
from abstract import Component, Visitor

class DornellesVisitor(Visitor):
    def resolve_component_a(self, element: Component):
        print(f"{__class__.__name__} visitou {element.__class__.__name__}")

    def resolve_component_b(self, element: Component):
        print(f"{__class__.__name__} visitou {element.__class__.__name__}")

class AbdielVisitor(Visitor):
    def resolve_component_a(self, element: Component):
        print(f"{__class__.__name__} visitou {element.__class__.__name__}")

    def resolve_component_b(self, element: Component):
        print(f"{__class__.__name__} visitou {element.__class__.__name__}")
