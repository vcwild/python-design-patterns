from datetime import datetime
from interfaces import IService, Response


class Service(IService):
    def request(self) -> Response:
        print(f"Requesting response from {self.__class__.__name__}")
        return Response


class Proxy(IService):
    def __init__(self, real_service: Service):
        self.__real_service = real_service
        self.cached = False

    def request(self) -> Response:
        self.check_access()
        
        if not self.cached:
            self.cached = self.__real_service.request()
            self.log_access()

            return self.cached
        
        print(f"Response is already cached at: {self.log_time}")

        return self.cached
    
    def check_access(self) -> None:
        print(f"{self.__class__.__name__} is checking access prior to firing request")

    
    def log_access(self) -> None:
        self.log_time = datetime.utcnow()

        print(f"{self.__class__.__name__} is logging the time of request: {self.log_time}")