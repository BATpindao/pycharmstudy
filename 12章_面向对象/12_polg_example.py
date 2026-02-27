"""
多态的介绍：
子类继承父类并重写父类的方法，当通过父类引用调用方法时，不同子类对象会有不同的实现方式，这种现象就是多态。
"""

class Animal:
    def cry(self):
        pass

class Cat(Animal):
    def cry(self):
        print('小猫 喵喵叫')

class Dog(Animal):
    def cry(self):
        print('小狗 汪汪叫')

class Bird(Animal):
    def cry(self):
        print('小鸟 喳喳叫')

class Pig:
    def cry(self):
        print('小猪 噜噜叫')



# 注意 在python 面向对象中，子类对象可以传递给父类类型
def func(a:Animal):
    a.cry()

# 创建四个对象
c = Cat()
d = Dog()
b = Bird()
p = Pig()

# 调用函数
func(c)
func(d)
func(b)

# 解释 pig这个类型没有继承Animal这个类，这执行成功了，是因为 pig类中有cry()z这个方法
func(p)

"""
特别说明 python 多态的特点：
1.python中函数/方法的参数是没有类型限制的，所以多态在python中的体现并不是很严谨（比如和Java等强类型语言相比）
2.python并不要求严格的继承体系，关注的并不是对象的类型本身，而是他是否具有要调用的方法本生（行为）
"""