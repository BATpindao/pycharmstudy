"""
构造方法：
构造方法(构造器)基本语法：
def  __init__(self,参数列表):
    代码

1.一个类只有一个__init__方法，即使你写了多个，也只有最后一个生效，会覆盖
"""


# class Person:
#     name = None
#     age = None
#     # 构造方法/构造器
#     # 构造方法是完成对象的初始化任务
#     # self就是当前创建的对象
#     def __init__(self, name, age):
#         print(id(self))
#         # 把接受到的值赋值给属性
#         self.name = name
#         self.age = age
#         print('__init__执行了',name,age)
#     def __init__(self, name):
#         print('__init__执行了',name)
#
# #这里执行的话就会报错 我需要两个参数 但是给了三个
# p1 = Person('kobe',20)
# print(id(p1))
# print(p1.name,p1.age)


# python可以动态的生成对象属性
class Person:

    def __init__(self, name, age):
        # 将接收到的值 name,age 赋值给当前对象的 name和age
        # python支持动态生成对象属性,有返回值就会报错，就是返回一个控对象None
        # 构造方法不能有返回值
        self.name = name
        self.age = age
        print('__init__执行了',name,age)


#这里执行的话就会报错 我需要两个参数 但是给了三个
p1 = Person('kobe',20)
print(p1.__init__(1,2))