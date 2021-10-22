from abstract_objects import Observer, Subject


class CanturilObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 4:
            print(f"{self.__class__.__name__} reagiu ao {subject.__class__.__name__}")


class LukempolObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state <= 2:
            print(f"{self.__class__.__name__} reagiu ao {subject.__class__.__name__}")


class BrancoObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state > 5:
            print(f"{self.__class__.__name__} reagiu ao {subject.__class__.__name__}")


class AndressaObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state > 8:
            print(f"{self.__class__.__name__} reagiu ao {subject.__class__.__name__}")


class SalesObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 7:
            print(f"{self.__class__.__name__} reagiu ao {subject.__class__.__name__}")
