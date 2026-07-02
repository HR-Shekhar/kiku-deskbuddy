# It should only know how to talk to the OLED hardware.
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106


class OLEDDisplay:
    def __init__(self):
        serial = i2c(port=1, address=0x3C)
        self.device = sh1106(serial)

    def get_device(self):
        return self.device