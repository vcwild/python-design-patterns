from director import Director
from builders.modern import ModernBuilder
from builders.vintage import VintageBuilder


def main(builder):
    director = Director()

    director.builder = builder

    director.build_minimal()

    builder.product.get_parts()

    director.build_complete()

    director.build_accessories()

    builder.product.get_parts()



if __name__ == "__main__":

    builder = VintageBuilder()

    main(builder)

    builder = ModernBuilder()

    main(builder)
