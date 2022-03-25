from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def execute(self):
        pass
