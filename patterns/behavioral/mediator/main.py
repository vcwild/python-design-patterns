from components import AnotherComponent, SpecificComponent
from mediator import ConcreteMediator


specific = SpecificComponent()
another = AnotherComponent()

mediator = ConcreteMediator(component_1=specific, component_2=another)

if __name__ == "__main__":

    print("Another component is being triggered")
    specific.do_this()

    # print("Specific component is being triggered")
    # specific.do_this()
