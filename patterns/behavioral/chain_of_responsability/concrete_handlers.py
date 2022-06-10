from handler import BaseHandler


class AmandaHandler(BaseHandler):
    def handle(self, request) -> str:
        if request == "lasanha":
            return f"{__class__.__name__} atendeu {request}!"
        return super().handle(request)


class CafeHandler(BaseHandler):
    def handle(self, request):
        if request in ["cafe", "cerveja"]:
            return f"{__class__.__name__} atendeu {request}!"
        return super().handle(request)


class KattHandler(BaseHandler):
    def handle(self, request):
        if request == "java":
            return f"{__class__.__name__} atendeu {request}!"
        return super().handle(request)


class DornellesHandler(BaseHandler):
    def handle(self, request):
        if request in ["3bc", "cachaça"]:
            return f"{__class__.__name__} atendeu {request}!"
        return super().handle(request)


class CanturilHandler(BaseHandler):
    def handle(self, request):
        if request == "agua":
            return f"{__class__.__name__} atendeu {request}!"
        return super().handle(request)
