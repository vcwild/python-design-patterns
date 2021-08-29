from interface import TV, Radio
from bridge import AdvancedRemote, Remote
from typing import Union


def run(remote: Union[Remote, AdvancedRemote]) -> None:
    if isinstance(remote, AdvancedRemote):
        return print(remote.op_mute())

    print(remote.op_click())


if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    remote_tv = Remote(tv)
    remote_radio = Remote(radio)

    run(remote_tv)
    run(remote_radio)

    advanced_remote_tv = AdvancedRemote(tv)
    advanced_remote_radio = AdvancedRemote(radio)

    run(advanced_remote_tv)
    run(advanced_remote_radio)
