from abc import abstractclassmethod, ABC


class API:
    def request(self) -> str:
        return "Retorno com comportamento padrão"


class Service:
    def specific_request(self):
        return "laicepse otium oãçisiuqer amU"


class AbstractAdapter(ABC):
    @abstractclassmethod
    def request(self) -> str:
        ...


class Adapter(AbstractAdapter):
    def __init__(self) -> None:
        super().__init__()
        self.service = Service()

    def request(self) -> str:
        return f"Adaptando: {self.service.specific_request()[::-1]}"


def client_code(api: API) -> None:
    print(api.request())


api = API()

client_code(api)

adapter = Adapter()

client_code(adapter)
