from service import service
from interfaces import IService, Response


def client_code(service: IService) -> Response:
    response = service.request()

    return response


res = client_code(service)

print(res)
