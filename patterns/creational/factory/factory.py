from abstract_classes import Creator, Product


class MyConcreteCreator(Creator):
    def factory_method(self):
        product = MyConcreteProduct()
        return product


class MyOtherConcreteCreator(Creator):
    def factory_method(self):
        product = MyOtherConcreteProduct()
        return product


class MyDivulgatorsCreator(Creator):
    def factory_method(self):
        product = MyDivulgatorsProduct()
        return product


class MyConcreteProduct(Product):
    def operation(self):
        return "My concrete Product"


class MyOtherConcreteProduct(Product):
    def operation(self):
        return "My other concrete Product"


class MyDivulgatorsProduct(Product):
    def operation(self):
        return "Lives"
