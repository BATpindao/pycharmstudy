"""
什么是魔术方法：
    1.在python中，所有以双下划线__包起来的方法，统称为Magic method (魔术方法)  ，他是一种特殊的方法，
    普通方法需要调用，而魔术方法不需要调用就可以自动执行
    2.魔术方法在类或对象的某些事情发生时会自动执行，让类具有神奇的魔力 ， 如果希望自己的程序定制特殊功能的类，那么需要对这些方法进行重写
    3.python中常用的运算符，for循环，以及类操作等都是运行在魔术方法之上的
"""

class Person:
    # __new__ 比 __init__ 更早执行  执行顺序 __new__ 创建对象 -> __init__初始化对象
    def __new__(cls, *args, **kwargs):
        print('创建对象')
        return super().__new__(cls)

    # __init__ 对象创建时会自动执行
    def __init__(self, name, age):
        print('初始化对象')
        self.name = name
        self.age = age

    """
    解释：
    1.在默认情况下调用的是父类object的 __str__
    2.父类的object 的 __str__ 返回的就是类型 + 地址
    """
    def __str__(self):
        # print(hex(id(self)))
        # return super().__str__()
        return f'{self.name}, {self.age}'

    def __eq__(self, other):
        # 用于判断两个对象都是同一个类
        if isinstance(other,Person) :
            return self.name == other.name and self.age == other.age
        else:
            return False
        # 父类的__eq__()方法是内存地址的比较
        # return super().__eq__(other)


p = Person('tom',23)
p2 = Person('tom',23)

print(p)


# 1.== 是一个比较运算符，对象之间进行比较时，比较的是内存是否相等，即判断是不是同一个对象
# 2.重写 __eq__方法，可以用于判断对象内容/属性是否相等
print(p == p2)
"""
一般开发只重写：__init__  
__new__ 一般用于：
    单例模式
    控制对象创建
"""