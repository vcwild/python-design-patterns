from strategy import Car, Bike, Bus
from context import Context

car = Car()

bike = Bike()

bus = Bus()

strategies = [
    car, bike, bus
]

context = Context()


for strategy in strategies:

    context.set_strategy(strategy)
    context.execute(0, 200)
