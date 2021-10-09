from abstract_objects import AbstractChair, AbstractTable


class ModernChair(AbstractChair):
    def sit(self) -> str:
        return "Sentei na cadeira moderna"


class ModernTable(AbstractTable):
    def play_truco(self) -> str:
        return "Joguei truco na mesa moderna"

    def break_table(self, tool: AbstractChair) -> str:
        res = tool.sit()
        return f"A mesa foi quebrada por evento: {res}"


class VintageChair(AbstractChair):
    def sit(self) -> str:
        return "Sentei na cadeira vintage"


class VintageTable(AbstractTable):
    def play_truco(self) -> str:
        return "Joguei um truco meio vintage"

    def break_table(self, tool: AbstractChair) -> str:
        res = tool.sit()
        return f"A mesa foi quebrada por evento: {res}"
