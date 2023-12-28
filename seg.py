# name: seg.py
# author: Ashitaka
# interface: show
# ver: 1.0
# 实例化Seg当传入a,b,c,d,e,f,g,dp对应的接线针脚id元组,否则采用默认值
# 再者采用show方法驱动Seg显示相应的数字,如mine_seg.show(1)显示1,mine_seg.show("opne")全显示


from machine import Pin
from time import sleep


class Seg:
    """一只数码管的类"""

    def __init__(self, led_pins = (13, 12, 14, 27, 26, 25, 33, 32), com = 0):
        """
        初始化数码管,设置引脚对应逻辑功能
        led_pins一次对应(a,b,c,d,e,f,g,do)
        com代表共阳阴极,0共阴,1共阳
        """ 
        
        # 引脚对应功能 led_list[0,1,2,3,4,5,6,7,8]-->log[a,b,c,d,e,f,g,dp]
        self._led_list = [Pin(i, Pin.OUT) for i in led_pins]
        
        # 对应显示数字
        self.num_dict = {0: "11111100",1: "01100000",2: "11011010",3: "11110010",4: "01100110",5: "10110110",6: "10111110",7: "11100000",8: "11111110",9: "11110110",'.':"00000001","open": "11111111","close": "00000000"}

        # 对应共极
        self._com = com

        # 初始化Seg状态
        self._stats_init()


    def _stats_init(self):
        """初始化Seg,即将其led全灭(代码具有普适性,都初始化,而非简答的全灭),注意不可以用_show/show方法,否则导致循环调用"""
        i = 0
        for bit in self.num_dict["close"]:
            self._led_list[i].value(int(bit) ^ self._com)
            i += 1


    def _show(self, choice):
        """最简化无异常检测"""
        # 初始化loop参数
        i = 0
        _value = self.num_dict[choice]

        # 初始化Seg
        self._stats_init()    #此段必须位于get(choice)之下,由此实现:若无效显示要求,则保证原来的状态,而在是有效要求方初始化Seg

        # 将每位led设置成相应的状态
        for bit in _value:
            self._led_list[i].value(int(bit) ^ self._com)
            i += 1


    def show(self, choice):
        """显示字符,当非给定字符时则略过"""
        try:
            self._show(choice)
        except KeyError:
            pass


if __name__ == "__main__":
    # 创建实例
    mine_seg = Seg()
    # 遍历show函数
    for choice in mine_seg.num_dict.keys():
        mine_seg.show(choice)
        sleep(0.5)
    # 尝试异常值
    mine_seg.show(11)
    mine_seg.show("ALL")


