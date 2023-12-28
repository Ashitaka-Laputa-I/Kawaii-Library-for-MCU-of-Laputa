# name: Servo
# author: Ashitaka
# interface: set, init, read, rotate


from machine import Pin, PWM
from time import sleep_ms


class Servo:
    """舵机类,仅留存设置,clockwise """
    def __init__(self, pin, min_angle=0, max_angle=180, min_duty=1950, max_duty=8190, frequency=50, default_angle=0):
        """初始化舵机"""
        # pin: 输入引脚
        # frequency: 频率,sg90系列脉冲周期为20ms,由此默认设置50hz

        # 初始化配置
        self._pwm = PWM(Pin(pin))
        self._pwm.freq(frequency)

        # 设置角度及其对应占空比
        self._min_angle = min_angle
        self._max_angle = max_angle

        self._min_duty = min_duty
        self._max_duty = max_duty

        self._default_angle = default_angle

        # 计算占空比对角度的微分
        self._speed_duty = (self._max_duty - self._min_duty) / (self._max_angle - self._min_angle)

        # 初始化舵机角度
        self.set(self._default_angle)

        # 记录舵机当前角度, 并且初始化为默认值
        self._angle = self._default_angle



    def _angle_to_duty(self, angle):
        """将角度转化为相应的占空比,并且设置当前角度,此函数仅为set调用,其他慎用:注意角度设置的副作用!"""
        # 超越最大角则返回最大占空比
        if angle <= self._min_angle:
            self._angle = self._min_angle
            return self._min_duty
        # 低于最小角则返回最小占空比
        elif angle >= self._max_angle:
            self._angle = self._max_angle
            return self._max_duty
        # 线性模型,不是那么精确
        else:
            self._angle = angle
            return round(self._speed_duty * (angle - self._min_angle) + self._min_duty)


    def set(self, angle):
        """设置舵机角度0-180"""
        self._pwm.duty_u16(self._angle_to_duty(angle))


    def init(self):
        """舵机回归初始角"""
        self.set(self._default_angle)


    def read(self):
        """读取当前的角度"""
        return self._angle


    def rotate(self, angle):
    # 正逆时针转动,负顺时针转动
        self.set(self._angle + angle)


if __name__ == "__main__":
    # 设置默认值为90度舵机
    mine_servo = Servo(2, default_angle=90)
    sleep_ms(2000)

    #TODO:是否需要吗sleep内嵌到set中,还要计算时间,算了XD
    print(mine_servo.read())

    # 逆时针20度
    mine_servo.rotate(20)
    sleep_ms(2000)

    # 顺时针40度
    mine_servo.rotate(-40)
    sleep_ms(2000)

    # 回归初始角
    mine_servo.init()
    sleep_ms(2000)
    
    # 顺时针逐渐九十度
    for _ in range(90):
        mine_servo.rotate(-1)
        sleep_ms(20)
        
    # 逆时针逐渐一百八十度
    for _ in range(180):
        mine_servo.rotate(1)
        sleep_ms(20)
    
    # 逆时针逐渐旋转九十度
    for _ in range(90):
        mine_servo.rotate(-1)
        sleep_ms(20)
    
    # 初始化
    mine_servo.init()
    sleep_ms(1000)
    
    # 设置0度
    mine_servo.set(0)