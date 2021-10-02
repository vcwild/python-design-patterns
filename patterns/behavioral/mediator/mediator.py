from abc import ABC
from components import SpecificComponent, AnotherComponent


class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None: ...


class ConcreteMediator(Mediator):
    def __init__(self, component_1: SpecificComponent, component_2: AnotherComponent) -> None:
        self.component_1 = component_1
        self.component_1.mediator = self
        self.component_2 = component_2
        self.component_2.mediator = self

    def notify(self, sender: object, event: str):
        if event == "this":
            self.component_1.do_this()
        elif event == "that":
            self.component_1.do_that()
        elif event == "kick":
            self.component_2.do_kick()
        else:
            self.component_2.do_jump()
