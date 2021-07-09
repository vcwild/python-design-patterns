from caretaker import Caretaker
from originator import Originator

originator = Originator("originator-first-state")
caretaker = Caretaker(originator=originator)

def state_update_mockup(
    caretaker: Caretaker, originator: Originator, n_iter: int = 10
):
    for i in range(n_iter):
        caretaker.store_state() # Store the program state
        originator.alter_state() # Alter the program state

if __name__ == "__main__":
    state_update_mockup(caretaker, originator, 10) # Update `n` times the program state

    caretaker.store_state() # Store the last originator state

    caretaker.show_log() # Show all the logging states stored in the caretaker

    caretaker.undo() # Change the originator to the previous state

    caretaker.undo() # Change the originator to the state before the latest
