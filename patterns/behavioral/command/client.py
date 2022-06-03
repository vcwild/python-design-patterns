from command import CommandPaulo, CommandKasagari
from receiver import Receiver
from invoker import Invoker

# commands

receiver = Receiver()

kasagari = CommandKasagari("I am Kasagari")

paulo = CommandPaulo("Só os javeiros", receiver)

invoker = Invoker()
invoker.set_on_start(paulo)
invoker.set_on_finish(kasagari)

invoker.do_something()
