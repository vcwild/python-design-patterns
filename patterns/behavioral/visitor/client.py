from typing import NoReturn
from visitor import DornellesVisitor, AbdielVisitor
from components import ComponentA, ComponentB

def visit_all(components: list, visitor) -> NoReturn:
    for component in components:
        component.accept(visitor)

A = ComponentA()
B = ComponentB()

list_of_components = [A, B, A, B, B]

dornelles = DornellesVisitor()
visit_all(list_of_components, dornelles)

abdiel = AbdielVisitor()
visit_all(list_of_components, abdiel)
