"""
class对象基本介绍：
    1.类本身也是对象，即class对象

类定义执行后，会创建一个“类对象”
这个对象可以被访问、调用、或者用来创建实例

2.类对象可以做什么：
    。可以访问类属性
    。可以调用类方法
    。可以创建实例对象

"""


class Monster:
    name = "jak"
    age = 18

    """
    # 1. 实例对象调用（自动传参，最常用的写法）
    # 2. 类对象调用（必须手动传参，平时不常用，但能看懂底层逻辑）
    
    大白话原理解释
你可以把 self 想象成一张**“名片”**：
    .实例对象调用（比如 m1.hi()）： 就像是你亲自去办事，系统会自动把你的“名片”（实例对象本身）递给 hi() 方法，所以括号里啥也不用写。
    .类对象调用（比如 Monster.hi()）： 就像是公司（类）派人去办事，但没指名道姓派谁去。系统不会自动递名片，所以你必须手动把具体的员工（实例对象）填进括号里，比如 Monster.hi(m1)。如果不填，程序就会懵圈（报错缺少 positional argument），因为它不知道这个 self.name 到底该去读取谁的名字。
    """

    # 实例对象调用hi()方法，会隐式的将实例对象传进去；类对象去调用hi()方法时，必须手动把一个实例对象塞进括号里当参数传给 self，不然它不知道 self 指的是谁，会直接报错。
    def hi(self):
        print(f'hi() {self.name} {self.age}')


# <class '__main__.Monster'> 类对象  Monster本身是一个类对象, Monster的类型是 type：因为Monster是type创建出来的
print(Monster, type(Monster))

# <__main__.Monster object at 0x104635250> 示例对象
print(Monster(), type(Monster()))

# 通过class对象，可以引用属性
print(f'monster name:{Monster.name} age:{Monster.age}')

"""
讲解：Monster.hi(Monster) 为什么会弹提示信息
Monster.hi(Monster) 其实是手动调用了实例方法
上面这句话等价于：Monster.hi(self=Monster)
把
类对象 Monster
当成了
实例对象 self
传进去了

提示信息：Expected type 'Monster', got 'Type[Monster]' instead
我们翻译一下 👇
Expected type 'Monster'
👉 需要一个 Monster 实例对象
got 'Type[Monster]'
👉 结果给的是 “Monster这个类”
重点：
名字	            含义
Monster	        实例类型
Type[Monster]	类对象本身

也就是说 Monster不是一个实例，Type[Monster] 是一个类对象本身

def hi(self)
默认等价于 
def hi(self:Monster)
意思是
👉 self 必须是 Monster 的实例

5.那为什么代码还可以跑：
1.因为 Python 是动态语言。
2.运行时不会严格检查类型。
他只要发现传进来的对象有 name age 这两个属性存在，就可以运行成功

Monster        # 模具本身 （类对象）
Monster()      # 用模具造出来的东西 （实例对象）
"""
Monster.hi(Monster)

print('-' * 24)

"""
官方文档讲解：class对象
https://docs.python.org/zh-cn/3.13/tutorial/classes.html#private-variables

1.类变量 (class Variable)：
    类变量就是：属于整个类的共享实例(变量)，
所有对象对能看到同一份数据
"""


class Dog:
    kind = 'canine'  # 类变量

    def __init__(self, name, age):
        self.name = name
        self.age = age


d1 = Dog('大黄', 12)
d2 = Dog('小黑', 12)

# 实例对象调用
print(d1.kind)  # canine
print(d2.kind)  # canine
# 类对象调用
print(Dog.kind)  # canine
"""
结果都是一样的输出：canine 
应为 Dog.kind 只有一份，所有的实例都引用它
"""

"""
2.实例变量 (Instance Variable)
    实例变量就是：每个对象独立拥有的变量(值)
"""
# 每个对象对拥有自己的数据
print(d1.name)  # 大黄
print(d2.name)  # 小黑

"""
3.官方文档里的重点区别

| 类型   | 定义位置     | 是否共享   |
| ---- | -------- | ------ |
| 类变量  | class 里面 | 所有实例共享 |
| 实例变量 | self.xxx | 每个对象独立 |
"""
Dog.kind  # -> 类变量
d1.name  # -> 实例变量

"""
4.访问顺序 (非常重要)
python的变量访问顺序是：
对象 -> 类

1 先找 d.kind
2 找不到
3 再找 Dog.kind
"""

"""
5.实例可以覆盖类变量
d1.kind 原值 canine
"""
# d1.kind 给自己的 kind变量重新赋值了 i am king，覆盖了原来的 canine 所以他输出 i am king
d1.kind = 'i am king'
print(d1.kind)  # i am king
# 他没有做任何的操作，所以还是输出 canine
print(d2.kind)  # canine 还是用的是类提供的值

"""
6.官方文档里的经典坑（重点）
    不要用变量存 可变对象
"""


class Cat:
    tricks = []

    def add_trick(self, trick: str):
        self.tricks.append(trick)


c1 = Cat()
c2 = Cat()

c1.add_trick('狸花猫')
c2.add_trick('大胖橘')

"""
两个只猫的名字全部混在一起了
原因：
Dog.tricks = [] (可变类型) 只有一份
结构：
Dog
 └─ tricks = []

d1 -> 引用同一个
d2 -> 引用同一个

所以一个变全部都变
正确的写法
class Dog:
    def __init__(self):
        self.tricks = [] #互不影响
    def add_trick(self, trick):
        self.tricks.append(trick)
"""
print(c1.tricks)  # ['狸花猫', '大胖橘']
print(c2.tricks)  # ['狸花猫', '大胖橘']


"""
八、什么时候用类变量？

类变量适合：
    所有对象共享的数据
比如：
class Student:
    school = "Harvard"
或者统计数量：
class User:
    count = 0
    def __init__(self):
        User.count += 1
"""

"""
总结：
1 类变量：属于类，所有实例共享。
    class A:
    x = 1
    
2 实例变量：属于对象，每个对象独立。
    self.x = 1
    
3 注意可变对象：否则所有实例共用一个列表。
注意⚠️：不要这么写
    class A:
    list = []
"""