from state import ConcreteStateOne, ConcreteStateTwo, Context

context = Context(ConcreteStateOne())

context.try_reading()
context.try_reading()
context.try_writing()
context.move_to(ConcreteStateTwo())
print(f"I am at context: {context}")
