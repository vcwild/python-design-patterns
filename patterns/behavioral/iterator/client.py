from iterator import WordsCollection
from random_iterable import RandomIterable


def create_collection(elements: list[str]) -> WordsCollection:

    collection = WordsCollection()
    for element in elements:
        collection.add_item(element)

    return collection


if __name__ == "__main__":
    elements = ["gugah", "jiyu", "edujr", "b1ndh", "damiao"]
    collection = create_collection(elements)

    random_iterable = RandomIterable(elements)

    # next(random_iterable)

    for e in collection:
        print(e)
