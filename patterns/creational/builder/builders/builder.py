from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    def product(self) -> None: ...

    @abstractmethod
    def produce_hat(self) -> None: ...

    @abstractmethod
    def produce_shirt(self) -> None: ...

    @abstractmethod
    def produce_pants(self) -> None: ...

    @abstractmethod
    def produce_shoes(self) -> None: ...
