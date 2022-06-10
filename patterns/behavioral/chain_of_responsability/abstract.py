from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        ...

    @abstractmethod
    def handle(self, request):
        ...
