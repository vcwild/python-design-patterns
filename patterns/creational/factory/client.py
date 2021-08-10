from factory import (Creator,
                     MyConcreteCreator,
                     MyDivulgatorsCreator,
                     MyOtherConcreteCreator)


def client_code(creator: Creator) -> None:
    print("Calling creator {} \noperation: {}"
          .format(creator.__class__, creator.some_operation()))


if __name__ == "__main__":
    creator = MyConcreteCreator()
    client_code(creator)

    creator = MyOtherConcreteCreator()
    client_code(creator)

    creator = MyDivulgatorsCreator()
    client_code(creator)
