"""
python 魔术方法 GPT AI 🪄
"""

# 被双下划线包围的方法 就是魔术方法

# __init__(初始化方法)   __new__ (创建对象)
class Person:
    def __init__(self, name, age):
        print('初始化对象')
        self.name = name
        self.age = age
    def __new__(cls, name, age):
        print('创建对象')
        return object.__new__(cls)

# __new__ 执行顺序大于 __init__
p = Person('tom',12)


print()
# 2.字符串显示相关 (常用)
"""
__str__ --打印对象
"""
class Cat:
    def __init__(self, name):
        self.name = name

    # __str__是给用户看的
    def __str__(self):
        return f'小猫的名字：{self.name}'
    # __repr__ 是给程序员看的 执行顺序： __str__ -> __repr__  如果没有__str__ 就会执行__repr__
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

c = Cat('咪咪')
# 没有重写之前的输出： <__main__.Cat object at 0x107a65160>
# 重写 __str__之后 小猫的名字：咪咪
print(c)

# 练习题 __str__
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'学生：{self.name}，成绩：{self.score}'

s = Student('jek',100)
print(s)


print()
# 3.运算符重载  (重点🔥)
class Vector:
    def __init__(self, x):
        self.x = x

    # +
    def __add__(self, other):
        # 返回这里是 写的类名
        return Vector(self.x + other.x)
    # -
    def __sub__(self, other):
        return Vector(self.x - other.x)

    # *
    def __mul__(self, other):
        return Vector(self.x * other.x)

    # /
    def __truediv__(self, other):
        return Vector(self.x / other.x)

    # ==
    def __eq__(self, other):
        return self.x == other.x

    # >
    def __gt__(self, other):
        return self.x > other.x

    # <
    def __lt__(self, other):
        return self.x < other.x

    def __str__(self):
        return f'Vector({self.x})'


v1 = Vector(10)
v2 = Vector(20)
v3 = v1 + v2
# 等价于 v1.__add__(v2)
# print(v1*v2)
# print(v1+v2)
print(v1<v2)


print()
# 4.容器相关(数组) (高级用法🔥🔥)

"""
__len__   __getitem__ 用法
"""
class Mylist:
    def __init__(self,data):
        self.data = data

    # 获取列表的长度
    def __len__(self):
        return len(self.data)

    #获取 数组的中的元素
    def __getitem__(self, item):
        return self.data[item]

    # 设置 某个位置元素的内容
    def __setitem__(self, key, value):
        self.data[key] = value

    def __str__(self):
        return str(self.data)

m = Mylist([1,2,3,4])
print(len(m))
print(m[2])
m[3] = 9
print(m)





