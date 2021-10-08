import copy


class MyComponent:
    def __init__(self, my_property, another_property, circular_ref):
        self.my_property = my_property
        self.another_property = another_property
        self.circular_ref = circular_ref

    def __copy__(self):
        another_property = copy.copy(self.another_property)
        circular_ref = copy.copy(self.circular_ref)

        new = self.__class__(self.my_property, another_property, circular_ref)

        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo: dict = {}):
        another_property = copy.deepcopy(self.another_property)
        circular_ref = copy.deepcopy(self.circular_ref)

        new = self.__class__(self.my_property, another_property, circular_ref)

        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


class RecursiveEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent
