from strategy import RouteStrategy


class Context:
    def __init__(self) -> None:
        self.__strategy: RouteStrategy

    @property
    def strategy(self) -> RouteStrategy:
        return self.__strategy
    
    def set_strategy(self, strategy: RouteStrategy) -> None:
        self.__strategy = strategy

    def execute(self, a: int, b: int) -> None:
        self.__strategy.execute(a, b)


