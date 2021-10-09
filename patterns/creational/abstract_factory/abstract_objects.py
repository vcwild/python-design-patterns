from abc import abstractmethod


class AbstractChair:
    @abstractmethod
    def sit(self) -> str:
        ...


class AbstractTable:
    @abstractmethod
    def play_truco(self) -> str:
        ...

    @abstractmethod
    def break_table(self, tool: AbstractChair):
        ...
