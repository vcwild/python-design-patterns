from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def click(self):
        ...

    @abstractmethod
    def mute(self):
        ...


class TV(Device):
    def click(self):
        return f"{self.__class__.__name__} clicked"

    def mute(self):
        return f"{self.__class__.__name__} muted"


class Radio(Device):
    def click(self):
        return f"{self.__class__.__name__} clicked"

    def mute(self):
        return f"{self.__class__.__name__} muted"
