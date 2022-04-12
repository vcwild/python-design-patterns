from json import dumps


class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        shared_state = dumps(self._shared_state)
        _unique_state = dumps(unique_state)
        print(
            f"Flyweight: Shared_state -> {shared_state}, unique_state -> {_unique_state}"
        )

    def __repr__(self) -> str:
        return f"Flyweight(shared_state={self._shared_state}) 🚗💨"


class FlyweightFactory:
    _flyweights = {}

    def __init__(self, initial_flyweights: list[list]):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: dict):
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state) -> Flyweight:
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print(
                f"\033[31mflyweight not found, creating a flyweight for: {key}\033[0m"
            )
            self._flyweights[key] = Flyweight(shared_state)
            return self._flyweights[key]
        print(f"flyweight found -> {self._flyweights[key]}")
        return self._flyweights[key]

    def show(self):
        print(f"our flyweight keys: {self._flyweights.keys()}\n")


class CarRegistry:
    @staticmethod
    def add_car(factory: FlyweightFactory, plate, owner, brand, model, color):
        flyweight = factory.get_flyweight([brand, model, color])
        flyweight.operation([plate, owner])
