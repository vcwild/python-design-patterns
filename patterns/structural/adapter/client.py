from adapter import Adapter
from adapter import API


def client_code(api: API) -> None:
    print(api.request())


api = API()

client_code(api)

adapter = Adapter()

client_code(adapter)
