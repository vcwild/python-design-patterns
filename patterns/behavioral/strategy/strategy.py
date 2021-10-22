from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int):
        ...


class Car(RouteStrategy):
    def execute(self, a: int, b: int):
        cost = 10
        result = b - a
        
        print(f"O deslocamento de {self.__class__.__name__} é: {result * cost} metros e custa R${cost * 10}")


class Bike(RouteStrategy):
    def execute(self, a: int, b: int):
        cost = 0
        result = b - a
        
        print(f"O deslocamento de {self.__class__.__name__} é: {result * 20} metros e custa R${cost * 0}")


class Bus(RouteStrategy):
    def execute(self, a: int, b: int):
        cost = 5
        result = b - a
        
        print(f"O deslocamento de {self.__class__.__name__} é: {result * cost * 3.5} metros e custa R${cost * 15}")
