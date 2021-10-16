from builders.builder import Builder


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal(self) -> None:
        self.builder.produce_shirt()
        self.builder.produce_pants()

    def build_complete(self) -> None:
        self.builder.produce_shirt()
        self.builder.produce_pants()
        self.builder.produce_hat()
        self.builder.produce_shoes()

    def build_accessories(self) -> None:
        self.builder.produce_hat()
        self.builder.produce_shoes()
