from abstract import Handler
from concrete_handlers import (
    AmandaHandler,
    CafeHandler,
    CanturilHandler,
    DornellesHandler,
    KattHandler,
)


def client_code(handler: Handler, elements: list[str]):
    for element in elements:
        print(f"For the {element} element")
        result = handler.handle(element)
        if result:
            print(f"result > {result}")
        else:
            print(f"{element} was not resolved!")


def main():

    box = ["pudim", "java", "3bc", "lasanha", "agua", "cafe", "cerveja", "cachaça"]

    amanda = AmandaHandler()
    dornelles = DornellesHandler()
    katt = KattHandler()
    cafe = CafeHandler()
    canturil = CanturilHandler()

    amanda.set_next(dornelles).set_next(canturil).set_next(katt).set_next(cafe)

    print("Starting the chain!! 🙍⛓️👱⛓️💁")
    client_code(amanda, box)


if __name__ == "__main__":
    main()
