from abstract_factory import AbstractFactory
from factories import ModernFactory, VintageFactory


def client_code(factory: AbstractFactory) -> None:
    chair = factory.create_chair()
    table = factory.create_table()

    print(f"{chair.sit()}")
    print(f"{table.play_truco()}")
    print(f"{table.break_table(chair)}")


if __name__ == "__main__":
    client_code(ModernFactory())

    client_code(VintageFactory())
