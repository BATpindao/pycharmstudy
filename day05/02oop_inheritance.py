"""
二、继承（Inheritance）——“站在巨人的肩膀上”
Python支持多继承，也因此带来了最经典的两个问题：菱形继承 & 方法解析顺序（MRO）

继承允许我们在已有类的基础上创建新类，并且新类可以继承父类的属性和方法，这样可以复用已有的代码，并对其功能进行拓展
关键概念：
.子类和父类：子类继承父类的属性和方法，子类还可以重写父类的方法
.super() : 可以用super()来调用父类的构造方法或父类的其他方法
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 在吃东西...")


class Flyable:
    def fly(self):
        print("我在飞！")


class Bird(Animal, Flyable):   # 多继承
    def __init__(self, name, color):
        super().__init__(name)     # 推荐写法 super代表父类
        self.color = color

    def sing(self):
        print("在唱歌～～")

    def eat(self):                 # 方法重写（override）
        print(f"{self.name} 优雅地啄食～")

"""
必须掌握的进阶内容：
1.super() 的两种常见用法（Python3推荐）
    .super().__init__(...)
    .super().方法名(...)（在多继承中特别有用）

2.方法解析顺序（MRO） — 一定要会看！Pythonprint(Bird.mro())           # 查看继承链
    # 通常输出：[<class '__main__.Bird'>, <class '__main__.Animal'>, <class '__main__.Flyable'>, <class 'object'>]
3.Python3中 super() 在多继承下是按 C3线性化 算法解析的，不是深度优先
"""

# 使用
b = Bird('兔子','blue')
b.eat()
b.sing()
b.fly()