from composite import Composite
from leaf import Leaf


list_of_components = [
    Composite().add([Leaf(), Composite().add([Leaf(), Leaf()])]),
    Leaf(),
    Leaf(),
]

composite = Composite()

composite.add(list_of_components)
composite.add(list_of_components)

composite.add(Leaf())

result = composite.execute()

print("my children: ", composite.children)
print(f"sum of leafs = {result}")
