from caretaker import Caretaker
from originator import Originator

originator = Originator("originator-first-state")
caretaker = Caretaker(originator=originator)

def state_update_mockup(
    caretaker: Caretaker, originator: Originator, n_iter: int = 10
):
    for i in range(n_iter):
        # Store the program state
        caretaker.store_state()

        # Alter the program state
        originator.alter_state()

if __name__ == "__main__":
    # Update `n` times the program state
    state_update_mockup(caretaker, originator, 10)

    # Store the last originator state
    caretaker.store_state()

    # Show all the logging states stored in the caretaker
    caretaker.show_log()

    # Change the originator to the previous state
    caretaker.undo()

    # Change the originator to the state before the latest
    caretaker.undo()
