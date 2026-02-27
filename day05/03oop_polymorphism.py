"""
三、多态（Polymorphism）——“同一个接口，不同实现”
Python的多态是鸭子类型（Duck Typing） + 方法重写 的结合，几乎不需要显式接口。

多态指的是同一个方法作用于不同的对象时，表现出不同的行为。多态通常通过继承和方法重写实现，在面向对象编程中非常重要。
关键概念：
.方法重写：子类可以重写父类的方法，实现不同的行为
.鸭子类型：python 是动态类型语言，他更关注对象能做什么，而不是他的类型。在多态中，你不需要关心对象的具体类型，只需要调用方法即可
"""
def make_noise(animal):
    animal.make_sound()   # 不关心是什么类型，只要有这个方法就行

class Dog:
    def make_sound(self):
        print("汪汪汪！")

class Cat:
    def make_sound(self):
        print("喵～")

class Robot:
    def make_sound(self):
        print("哔哔哔...")

make_noise(Dog())     # 汪汪汪！
make_noise(Cat())     # 喵～
make_noise(Robot())   # 哔哔哔...

print()

# Python多态的终极形态：抽象基类（ABC） + @abstractmethod
admin = [Dog(), Cat(), Robot()]
for a in admin:
    a.make_sound() #不同对象调用相同的方法，表现出不同的行为

print()
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("汪！")

# Animal()          # 报错！不能实例化抽象类
Dog().make_sound()   # 可以


"""
深入理解：
    .封装：通过合理使用私有属性和方法，保护对象的内部状态，保证数据的完整性和一致性了
    .继承：使得代码具备复用性，避免重复代码，并且通过重写父类方法，可以改变拓展父类的行为
    .多态：通过统一接口调用不同的类对象时，能够获得不同的结果，提高代码的灵活性和拓展性
"""

"""
快速对比总结表:
特性,核心目的,Python实现方式,强制程度,进阶关注点
封装,隐藏细节、保护数据,_ 、 __ 、 @property,约定式,property / dataclasses / pydantic
继承,代码复用、扩展,class 子(父) 、多继承、super(),完全支持,MRO、C3线性化、super陷阱
多态,接口统一、动态绑定,鸭子类型 + 方法重写 + ABC,最灵活,@abstractmethod、协议（typing.Protocol）
"""