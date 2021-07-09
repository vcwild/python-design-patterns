from originator import Originator


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def store_state(self) -> None:
        print(f"The caretaker is storing its state: {self._originator._state}")
        memento = self._originator.save()
        self._mementos.append(memento)

    def undo(self):
        if not len(self._mementos):
            return None

        memento = self._mementos.pop()

        try:
            self._originator.restore_state(memento)
        except BaseException:
            self.undo()

    def show_log(self):
        for memento in self._mementos:
            print(memento.get_name())
