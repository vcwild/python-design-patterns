from abc import ABC, abstractmethod

from datetime import datetime


class AbstractMemento(ABC):
    @abstractmethod
    def get_name(self): ...

    @abstractmethod
    def get_date(self): ...


class Memento(AbstractMemento):
    def __init__(self, state) -> None:
        self._state = state
        self._date = str(datetime.now())

    def get_name(self):
        return f"{self._date} | ({self._state[0:9]})"

    def get_date(self):
        return self._date

    def get_state(self):
        return self._state
