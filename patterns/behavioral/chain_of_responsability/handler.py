from abc import abstractmethod
from abstract import Handler


class BaseHandler(Handler):
    _next = None

    def set_next(self, handler: Handler) -> Handler:
        self._next = handler

        return handler

    @abstractmethod
    def handle(self, request):
        if self._next:
            return self._next.handle(request)

        return None
