# 1、编写A01，定义方法max_lst，实现求某个float 列表list = [1.1, 2.9, -1.9, 67.9]的最大值，并返回。
class A01:
    @staticmethod
    def max_list(sort_list):
        max_number = 0
        for i in range(len(sort_list)):
            if sort_list[i] > max_number:
                max_number = sort_list[i]
        return max_number


list1 = [1.1, 2.9, -1.9, 67.9]
print(A01.max_list(list1))

print()


# 2、编写类Book，定义方法update_price，实现更改某本书的价格，具体：如果价格>150，则更改为150，如果价格>100，更改为100，否则不变。
class Book:
    book_name = None
    book_price = None

    # 初始化方法
    def __init__(self, book_name, book_price):
        self.book_name = book_name
        self.book_price = book_price

    def update_price(self, price):
        if price > 150:
            self.book_price = 150
        elif price > 100:
            self.book_price = 100


b = Book('西游记', 120)
print(b.book_name, b.book_price)

b.update_price(110)
print(b.book_name, b.book_price)

print()


# 3、定义一个圆类Circle，定义属性：半径，提供显示圆周长功能的方法，提供显示圆面积的方法。
class Circle:
    ban = None

    def __init__(self, ban):
        self.ban = ban

    def show_zc(self):
        print('圆的周长：', 3.14159 * self.ban)

    def show_mj(self):
        print('圆的面积：', self.ban ** 2 * 3.14159)


c = Circle(3)
c.show_zc()
c.show_mj()

print()


# 4、编程创建一个Cal计算类，在其中定义2个成员变量表示两个操作数，定义四个方法实现求和、差、乘、商（要求除数为0的话，要提示）并创建对象，分别测试。
class Cal:
    number1 = None
    number2 = None

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        print(self.number1 + self.number2)

    def jian(self):
        print(self.number1 - self.number2)

    def chen(self):
        print(self.number1 * self.number2)

    def chu(self):
        if self.number2 != 0:
            print(self.number1 / self.number2)
        else:
            print('除数不能为0')

c_jia = Cal(1,2)
c_jia.sum()
c_jia1 = Cal(3,1)
c_jia1.jian()
c_jia2 = Cal(1,2)
c_jia2.chen()
c_jia3 = Cal(1,1)
c_jia3.chu()


print()
# 5、定义Music类，里面有音乐名name，音乐时长times属性，并有播放play功能，和返回本身属性信息的方法get_info。
class Music:
    name = None
    times =None
    def __init__(self, name, times):
        self.name = name
        self.times = times

    def play(self):
        print('正在播放：',self.name)

    def get_info(self):
        return {'name': self.name, 'times': self.times}

m = Music('甜甜的',4.00)

m.play()
print(m.get_info())


print()
# 6、分析下列代码输出结果。
class Demo:
    i = 100

    def m(self):
        self.i += 1
        j = self.i
        print("i =", self.i)
        print("j =", j)

d1 = Demo()
d2 = d1
d2.m()

print(d1.i)
print(d2.i)


print()
# 7、石头剪刀布游戏，0表示石头，1表示剪刀，2表示布。
import random

class Tom:
    def __init__(self):
        self.choices = ['石头','剪刀','布']

    def paly(self):
        user_choice = int(input('0表示石头，1表示剪刀，2表示布:'))
        if user_choice not in [0,1,2]:
            print('请输入规定范围的值...')
            return
        computer_choice = random.randint(0,2)

        if user_choice == computer_choice:
            print('平手')
        elif ((user_choice == 0 and computer_choice == 1)or
              (user_choice == 1 and computer_choice == 2) or
              (user_choice == 2 and computer_choice == 0)):
            print('你赢了')
        else:
            print('机器人赢了')

t = Tom()
t.paly()
