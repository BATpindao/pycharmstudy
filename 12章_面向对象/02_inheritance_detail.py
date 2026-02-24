# """
# 子类继承了父类所有的属性和方法，非私有的属性和方法可以在子类直接访问，但是私有的属性和方法不能在子类直接访问，要父类提供公共的方法去访问
# """
# class Base:
#     n =100
#     __n2 = 200
#
#     def __init__(self):
#         print('base的构造方法')
#
#     # 公共方法
#     def hi(self):
#         print('hi公共方法')
#
#     # 私有方法
#     def __hello(self):
#         print('hello私有方法')
#
#     # 提供一个公开的方法去访问，私有的属性，方法
#     def get_pulic(self):
#         print(self.__n2)
#         self.__hello()
#
# class Sub(Base):
#     def __init__(self):
#         print('sub构造方法')
#
#     def sub_on(self):
#         # 访问公共属性方法
#         print(self.n)
#         self.hi()
#
#         #访问私有属性方法
#         # self.__n2 这样直接访问父类的私有属性是访问不了的
#
# s = Sub()
# s.sub_on()
# s.get_pulic()


"""
python是支持多继承的
"""

class A:
    n = 100

    def sing(self):
        print('A构造方法：',self.n)


class B:
    n = 200
    n2 = 300

    def dance(self):
        print('B构造方法：', self.n)

    def sing(self):
        print('B构造方法：', self.n)


class C(B,A):
    pass

c = C()
print(c.n)
print(c.n2)

c.sing()
c.dance()

"""
在多继承中，如果有同名的成员，遵收从左到右的继承优先级（即：左边的父类优先级高，右边的父类优先级低）
"""