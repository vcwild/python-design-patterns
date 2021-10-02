class BaseComponent:
    def __init__(self, mediator=None) -> None:
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator) -> None:
        self._mediator = mediator


class SpecificComponent(BaseComponent):
    def do_this(self) -> None:
        print("SpecificComponent did this")
        self.mediator.notify(self, "this")

    def do_that(self) -> None:
        print("SpecificComponent did that")
        self.mediator.notify(self, "that")


class AnotherComponent(BaseComponent):
    def do_jump(self) -> None:
        print("AnotherComponent did jump")
        self.mediator.notify(self, "jump")

    def do_kick(self) -> None:
        print("AnotherComponent did kick")
        self.mediator.notify(self, "kick")
