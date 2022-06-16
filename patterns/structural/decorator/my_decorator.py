from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def execute(self):
        ...


class BaseComponent(Component):
    def execute(self):
        return f"executed: {__class__.__name__}!"


class BaseDecorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self):
        return self._component

    def execute(self):
        self._component.execute()


class DecoratorXiz(BaseDecorator):
    def execute(self):
        return f"executed: Xis decorator!\n{self.component.execute()}"


class DecoratorAmanda(BaseDecorator):
    def execute(self):
        return f"executed: Amanda decorator!\n{self.component.execute()}"


class DecoratorEduJr(BaseDecorator):
    def execute(self):
        return f"executed: EduJr decorator!\n{self.component.execute()}"


class DecoratorHenrique(BaseDecorator):
    def execute(self):
        return f"executed: Henrique decorator!\n{self.component.execute()}"


class DecoratorPassos(BaseDecorator):
    def execute(self):
        return f"executed: Passos decorator!\n{self.component.execute()}"


class DecoratorDallai(BaseDecorator):
    def execute(self):
        return f"executed: Dallai decorator!\n{self.component.execute()}"
