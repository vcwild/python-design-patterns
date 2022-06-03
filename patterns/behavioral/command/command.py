from abc import ABC, abstractmethod
from receiver import Receiver

class Command(ABC):
    @abstractmethod
    def execute(self): ...

class CommandKasagari(Command):
    def __init__(self, data):
        self._data = data

    def execute(self):
        print(f"{__class__.__name__}: called command with data: {self._data}")

class CommandPaulo(Command):
    def __init__(self, data: str, receiver: Receiver):
        self._data = data
        self._receiver = receiver

    def execute(self):
        print(f"{__class__.__name__}: called command with data: {self._data}")
        self._receiver.run_data(self._data)
