# class Cat:
#     name = '波斯喵'
#     age = 2
#     def info(self,name):
#         # 通过self.属性名 可以访问 对象的属性/成员变量
#         print('name的信息：',self.name)
#
# c = Cat()
# c.info('布偶')

"""
1.方法定义的参数列表中，有一个self
2.self是定义成员方法时，需要写上去的，如果不写，则需要用@staticmethod 标注，否则会报错
语法：
    class 类名：
        @staticmethod
        def f(arg1,arg2,arg3): ....

"""


class Dog:
    name = '金毛'
    age = 3

    def info(self, name):
        print(id(self))
        print(f'self信息：{name}')

    def eat(self):
        print(f'{self.name} 饿了。。。')

    def cry(self,name):
        print(f'{name} is crying...')
        print(f'{self.name} is crying...')
        self.eat()

    @staticmethod
    def ok():
        print(f'ok info..')


# 创建一个对象
d = Dog()
# 调用普通方法
d.info('边牧')

# 调用静态方法
d.ok()  # 通过对象调用

Dog().ok()  # 通过类名调用

"""
2.self表示当前对象本身，简单的说，那个对象调用，self就代表那个对象
"""
d2 = Dog()
d2.info('阿拉斯加')
print(id(d2))  # 这个 实力(d2) 的内存地址和 self的内存地址是一样的

print()
"""
1.通过对象调用方法时，self会隐试的传入
2.在方法内部访问成员变量，成员方法，需要使用self
"""
d3 = Dog()
d3.name = '中华田园犬'
d3.cry('金毛')
