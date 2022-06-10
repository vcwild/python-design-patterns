import random
from typing import Iterable


class RandomIterable(Iterable):
    def __init__(self, collection: list):
        self._collection = collection

    def __iter__(self):
        return self

    def __next__(self):
        value = random.choice(self._collection)
        return value
