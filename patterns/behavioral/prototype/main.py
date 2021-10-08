from prototype import RecursiveEntity, MyComponent
import copy

if __name__ == "__main__":
    object_list = [1, {1, 2, 3}, [1, 2, 3]]

    reference = RecursiveEntity()

    component = MyComponent("whatsapp2", object_list, reference)

    reference.set_parent(component)

    shallow_component = copy.copy(component)

    shallow_component.another_property.append("my string")

    print("component:\t\t", component.another_property)
    print("shallow_component:\t", shallow_component.another_property)

    shallow_component.another_property[1] = 22

    print("component:\t\t", component.another_property)
    print("shallow_component:\t", shallow_component.another_property)

    deep_component = copy.deepcopy(component)

    # print("component:\t\t", component.another_property)
    # print("deep_component:\t", deep_component.another_property)
