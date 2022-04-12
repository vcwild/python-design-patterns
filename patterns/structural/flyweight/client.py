from flyweight import FlyweightFactory, CarRegistry


factory = FlyweightFactory(
    [
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
        ["Chevrolet", "Chevette77", "grey"],
    ]
)

factory.show()

CarRegistry.add_car(factory, "AKL1234", "Canturil", "Gol", "Sapao2011", "blue")
CarRegistry.add_car(factory, "AKL1234", "Canturil", "Mercedes", "CLK 2020", "red")
CarRegistry.add_car(factory, "TESTE", "Flavia", "Mercedes", "CLK 2020", "red")
CarRegistry.add_car(factory, "OVF023984", "Vcwild", "Gol", "Sapao2011", "blue")

factory.show()
