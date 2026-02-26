"""
使用多态来遍写宠物喂食的程序
"""
# 食物
class Food:
    name = None

    def __init__(self, name):
        self.name = name


class Fish(Food):
    pass


class Bone(Food):
    pass


# 动物类
class Animal:
    name = None

    def __init__(self, name):
        self.name = name


class Cat(Animal):
    pass


class Dog(Animal):
    pass


# 人类
class Master:
    name = None

    def __init__(self, name:str):
        self.name = name

    def feed(self, animal: Animal, food: Food) -> str:
        return f'主人{self.name} 正在给宠物：{animal.name} 喂食：{food.name}'


m = Master('jek')
c = Cat('狸花猫')
f = Fish('黄花鱼')
d = Dog('京巴')
bon = Bone('肋排')

# 输出日志
print(m.feed(c,f))
print(m.feed(d,bon))

"""
多态的介绍：
1.多态顾名思义即多种状态，不同的对象调用相同的方法，表现出不同的状态，称为多态
2.多态通常作用在继承关系上
3.举例：一个父类，具有多个子类，不同的子类对象调用相同的方法，执行的时候产生不同的状态，就是多态
子类继承父类，并重写父类的方法，当使用父类类型调用方法时，不同的子类对象会表现出不同的行为，这种现象就是多态
"""