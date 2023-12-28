# name: Led
# author: Ashitaka
# interface: on, off, switch


from machine import Pin


class Led:
	"""封装的Led类,对外仅留存on,off,switch与read接口"""
	def __init__(self, pin, mode=0):
		"""初始化Led"""
		# pin: 输出引脚
		# mode: 0代表共阴极, 1代表共阳极

		# 设置值
		self._pin = Pin(pin, Pin.OUT)	
		self._mode = mode

		# 初始化值
		self._pin.off()


	def on(self):
		"""Led On"""
		self._pin.value(not mode)


	def off(self):
		"""Led Off"""
		self._pin.value(mode)


	def switch(self):
		"""Led Switch"""
		self._pin.value(not self._pin.value())


	def read(self):
		"""Led Value注意,我们始终以0代表LED熄灭,1代表LED明亮"""
		return self._pin.value() ^ self._mode