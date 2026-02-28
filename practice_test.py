from pyclbr import Class


class Cat:
    def __new__(cls, *args, **kwargs):
        print('开始创建小猫对象')
        return super().__new__(cls)
    def __init__(self, name):
        self.name = name
        print('初始化小猫属性')

c = Cat('mao')
