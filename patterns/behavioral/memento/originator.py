from memento import Memento

from random import sample

from string import ascii_letters


class Originator:
    def __init__(self, state) -> None:
        self._state = state
        print(f"The originator current state is: {self._state}")

    def alter_state(self) -> None:
        self._state = self._generate_random_string()
        print(f"The originator state has changed to: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self):
        return Memento(self._state)

    def restore_state(self, memento: Memento):
        self._state = memento.get_state()
