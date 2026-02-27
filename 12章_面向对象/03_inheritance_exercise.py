"""
练习题:
编写Computer类，包含CPU、内存、硬盘等属性  5min
1) get_details方法用于返回Computer的详细信息
2) 编写PC子类，继承Computer类，添加特有属性【品牌brand】
3) 编写NotePad子类，继承Computer类，添加特有属性【color】
4) 完成测试，创建PC和NotePad对象，分别给对象中特有的属性赋值，以及从Computer类继承的属性赋值，并使用方法打印输出信息
"""

class Computer:
    def __init__(self,cpu,nc,ddr4):
        self.cpu = cpu
        self.nc = nc
        self.ddr4 = ddr4

    def get_details(self):
        return f'cpu:{self.cpu},内存:{self.nc}，硬盘：{self.ddr4}'

class Pc(Computer):
    def __init__(self,brand,cpu,nc,ddr4):
        self.brand = brand
        super().__init__(cpu,nc,ddr4)

    def get_info(self):
        print(f'品牌：{self.brand} {self.get_details()}')
        self.get_details()

class NotePad(Computer):
    def __init__(self,color,cpu,nc,ddr4):
        self.color = color
        super().__init__(cpu,nc,ddr4)
    # 输出电脑信息
    def get_info(self):
        print(f'颜色：{self.color} {self.get_details()}')


p = Pc('ROG','iter14','128G','8T')
p.get_info()

n = NotePad('red','晓龙888','64G','1T')
n.get_info()