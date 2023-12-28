# name: PS2 Controller
# author: Ashitaka
# interface: read


from machine import Pin, ADC
from time import sleep_ms


class PS2Controller:
	"""PS2手柄模块"""
	def __init__(self, x_pin, y_pin, b_pin, range = ADC.ATTN_11DB):
		"""初始化"""
		# x_pin: x轴输出引脚
		# y_pin: y轴输出引脚
		# b_pin: button输出引脚
		# range: 量程,默认3.3v
		
		# ADC.ATTN_0DB— 满量程电压：1.2V
		# ADC.ATTN_2_5DB— 满量程电压：1.5V
		# ADC.ATTN_6DB— 全量程电压：2.0V
		# ADC.ATTN_11DB— 全量程电压：3.3V

		self._x_out = ADC(Pin(x_pin))
		self._x_out.atten(range)
		self._y_out = ADC(Pin(y_pin))
		self._y_out.atten(range)
		self._b_out = Pin(b_pin, Pin.IN)


	def read(self):
		"""读取三元组的数据"""
		return self._x_out.read(), self._y_out.read(), self._b_out.read()


if __name__ == "__main__":
	mine_ps2 = PS2Controller(33, 32, 15)

	while True:
		print(mine_ps2.read())
		sleep_ms(100)


