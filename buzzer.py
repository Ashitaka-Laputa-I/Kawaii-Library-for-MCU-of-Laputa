from machine import Pin, PWM
from time import sleep_ms

class Buzzer:
    """变调蜂鸣器"""
    def __init__(self, input_pin, mode=1):
        """ 初始化"""
        
        # input_pin: io输入引脚
        # mode: 1代表高电压触发,0代表低电压触发
        
        # 设置pwm
        self._pwm = PWM(Pin(input_pin, Pin.OUT))

        # 触发模式
        self._mode = mode

        # 音符-频率字典
        self._note_frequency = {
            "B0": 31, "C1": 33, "CS1": 35, "D1": 37, "DS1": 39, "E1": 41, "F1": 44, "FS1": 46, "G1": 49, "GS1": 52, 
            "A1": 55, "AS1": 58, "B1": 62, "C2": 65, "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87, "FS2": 93, 
            "G2": 98, "GS2": 104, "A2": 110, "AS2": 117, "B2": 123, "C3": 131, "CS3": 139,"D3": 147, "DS3": 156, 
            "E3": 165, "F3": 175, "FS3": 185, "G3": 196, "GS3": 208, "A3": 220, "AS3": 233, "B3": 247, "C4": 262, 
            "CS4": 277, "D4": 294, "DS4": 311, "E4": 330, "F4": 349, "FS4": 370, "G4": 392, "GS4": 415, "A4": 440, 
            "AS4": 466, "B4": 494, "C5": 523, "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698, "FS5": 740, 
            "G5": 784, "GS5": 831, "A5": 880, "AS5": 932, "B5": 988, "C6": 1047, "CS6": 1109, "D6": 1175, "DS6": 1245, 
            "E6": 1319, "F6": 1397, "FS6": 1480, "G6": 1568, "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976, "C7": 2093, 
            "CS7": 2217, "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794, "FS7": 2960, "G7": 3136, "GS7": 3322, "A7": 3520, 
            "AS7": 3729, "B7": 3951, "C8": 4186, "CS8": 4435, "D8": 4699, "DS8": 4978
        }

        # 初始化默认不触发
        self._pwm.duty(not self._mode)



    def _play(self, note, rest, duty):
        """播放单音符"""
        if note in self._note_frequency:
            self._pwm.freq(self._note_frequency[note])
            self.self._pwm.duty(duty)
        else:
            pass    # 即空,但依旧占用相应的时间
        # 延音
        sleep_ms(rest)
         # 初始化占空比
        self._pwm.duty(not self._mode)

    def play(self, staff, rest, duty = 512):
        """以duty占空比freq频率rest休止播放staff(无健壮性的异常处理机制)"""

        # 单音符
        if not isinstance(staff, list):
            self._play(staff, rest, duty)
        else:
            # 音符列表
            for note in staff:
                self._play(note, rest, duty)


if __name__ == "__main__":
    jingle = [
        "E7", "E7", "E7", "0",
        "E7", "E7", "E7", "0",
        "E7", "G7", "C7", "D7", "E7", "0",
        "F7", "F7", "F7", "F7", "F7", "E7", "E7", "E7", "E7", "D7", "D7", "E7", "D7", "0", "G7", "0",
        "E7", "E7", "E7", "0",
        "E7", "E7", "E7", "0",
        "E7", "G7", "C7", "D7", "E7", "0",
        "F7", "F7", "F7", "F7", "F7", "E7", "E7", "E7", "G7", "G7", "F7", "D7", "C7", "0"
        "F7", "F7", "F7", "F7", "F7", "E7", "E7", "E7", "E7", "D7", "D7", "E7", "D7", "0", "G7", "0",
    ]

    mine_buzzer = Buzzer(2)
    mine_buzzer.play(jingle, rest = 260)