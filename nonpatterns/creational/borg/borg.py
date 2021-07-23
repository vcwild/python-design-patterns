class Borg:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__


class AnotherBorg:

    _shared_state = {}

    def __new__(cls):
        instance = super().__new__(cls)
        instance.__dict__ = cls._shared_state
        return instance
