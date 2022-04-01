from interface import Device


class Remote:
    def __init__(self, device: Device):
        self.device = device

    def op_click(self) -> str:
        return f"Basic remote control operation with:\n" f"{self.device.click()}"


class AdvancedRemote(Remote):
    def op_mute(self) -> str:
        return f"Advanced remote control operation with:\n" f"{self.device.mute()}"
