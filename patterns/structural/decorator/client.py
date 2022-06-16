from my_decorator import (
    BaseComponent,
    DecoratorAmanda,
    DecoratorXiz,
    Component,
    DecoratorEduJr,
    DecoratorHenrique,
    DecoratorPassos,
    DecoratorDallai,
)


def main(component: Component):
    print(component.execute())


component = BaseComponent()
passos = DecoratorPassos(component)
xiz = DecoratorXiz(passos)
dallai = DecoratorDallai(xiz)
amanda = DecoratorAmanda(dallai)
edu = DecoratorEduJr(amanda)
henrique = DecoratorHenrique(edu)

"""
henrique  (decorator)
--------
edu       (decorator)
--------
amanda    (decorator)
--------
xiz       (decorator)
--------
component (impl)
"""

if __name__ == "__main__":
    main(henrique)
