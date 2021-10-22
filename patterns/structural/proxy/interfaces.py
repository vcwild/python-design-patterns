from abc import ABC, abstractmethod

class Response:
    ...


class IService(ABC):
    @abstractmethod
    def request(self) -> Response:
        ...
