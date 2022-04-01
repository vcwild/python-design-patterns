from abc import ABC, abstractmethod


class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def read(self):
        ...

    def write(self):
        ...


class ConcreteStateOne(State):
    def read(self):
        print("read one")
        self.context.move_to(ConcreteStateTwo())

    def write(self):
        print("write one")


class ConcreteStateTwo(State):
    def read(self):
        print("read two")

    def write(self):
        print("write two")
        self.context.move_to(ConcreteStateOne())


# Context(ConcreteStateOne).read() <-> Context(ConcreteStateTwo).write()
