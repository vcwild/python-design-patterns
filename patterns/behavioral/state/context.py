from state import State


class Context:
    def __init__(self, state: State):
        self.move_to(state)

    def __repr__(self):
        return f"Context({self._state.__class__.__name__})"

    def move_to(self, state: State):
        print(f"moving to {state.__class__.__name__}")
        self._state = state
        self._state.context = self

    def try_reading(self):
        self._state.read()

    def try_writing(self):
        self._state.write()
