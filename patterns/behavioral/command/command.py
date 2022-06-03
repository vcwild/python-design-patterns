from abc import ABC, abstractmethod

class Receiver:
    def run_data(self, data: str):
        print(f"Receiver received data: {data}")


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


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something(self):
        if self._on_start:
            print("Invoker started something!")
            self._on_start.execute()

        print("Invoker is doing something!")

        if self._on_finish:
            self._on_finish.execute()
            print("Invoker finished something!")
            return

        print("Invoker finished without on_finish!")
