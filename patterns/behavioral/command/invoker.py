from command import Command

class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something(self):
        if self._on_start:
            print("Invoker started something!")
            self._on_start.execute()

        print("Invoker is doing something!")

        if self._on_finish:
            self._on_finish.execute()
            print("Invoker finished something!")
            return

        print("Invoker finished without on_finish!")
