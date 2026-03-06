"""
抽象类的基本介绍：
1.默认情况下，python不提供抽象类，python附带一个模块，该模块为定义抽象基类提供了基础，该模块命名为 abc
2.当我们需要抽象基类时，让类继承ABC（abc模块的ABC类），使用@abstractmethod声明抽象方法
3.抽象类的价值更多作用于设计，是设计者设计好后，让子类继承并实现抽象类的抽象方法
"""
from abc import abstractmethod,ABC

# 动物类
class Animal(ABC):
    def __init__(self, name,age):
        self.name = name
        self.age = age

    # 这个时cry是一个抽象方法了
    @abstractmethod
    def cry(self):
        # 动物都有叫唤的行为...但是这个行为不明确(即不能明确的实现..)
        # print("不知道是什么动物, 不知道是什么叫声...")
        pass

# 注意抽象类不能被实例化，需要子类继承实现

class Dog(Animal):
    # 子类重写父类的抽象方法
    def cry(self):
        print(f'小狗汪汪汪汪叫，名字是，{self.name}')

d = Dog('大黄',3)
d.cry()

"""
注意：
1.抽象类不能被实例化
2.抽象类需要继承ABC，并且需要至少一个抽象方法
3.抽象类中可以有普通方法
4.如果一个类继承了抽象类，则它必须实现抽象类的所有抽象方法，否则它仍然是一个抽象类
"""