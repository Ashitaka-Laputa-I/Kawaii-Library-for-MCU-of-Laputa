from machine import Pin
from time import sleep_ms


class Button:
    """Button类"""
    def __init__(self, pin):
        self._pin = Pin(pin, Pin.IN)

    def read(self):
        """读取按钮激发状态1代表ON,0代表OFF"""
        if self._pin.value():
        	# 消抖
            sleep_ms(25)
            if self._pin.value():
                return 1
        return 0


if __name__ == "__main__":
    from time import sleep_ms
    mine_button = Button(27)
    
    while True:
        print(mine_button.read())
        sleep_ms(100)
