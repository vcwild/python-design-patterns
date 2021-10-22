from abc import ABC, abstractmethod
from random import randrange


class Observer(ABC):
    @abstractmethod
    def update(self, subject) -> None:
        ...


class Subject(ABC):
    _state: int
    _observers: list[Observer]

    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        ...

    def notify(self) -> None:
        ...
