from ctypes import Union
from typing import Any
from interface import Component


class Composite(Component):
    def __init__(self):
        self._children = []

    def __repr__(self) -> str:
        return f"Component(children={self._children})"

    @property
    def parent(self):
        return self.parent

    @parent.setter
    def parent(self, parent: Component):
        self.parent = parent

    def add(self, children: list[Component]):
        if isinstance(children, list):
            self._children.extend(children)
            return self

        self._children.append(children)
        return self

    def remove(self, child: Component):
        for c in self._children:
            if c is child:
                self._children.remove(c)

    @property
    def children(self):
        return self._children

    def execute(self) -> int:
        """
        Should traverse the entire tree and find `Leafs`.
        Should handle the value of each `Leaf` and add it to a sum.
        """
        result = 0
        for child in self._children:
            result += child.execute()
        return result
