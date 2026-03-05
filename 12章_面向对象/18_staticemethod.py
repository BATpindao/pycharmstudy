"""
静态方法：
1.@staticmethod 将方法转为静态方法
2.静态方法不会接收隐式的第一个参数，要什么一个静态方法，语法：
    @staticmethod
    def ok():
        print('ok()....')
3.静态方法既可以由 类调用 Monster.ok() 也可以由实例调用 m.ok()
"""
class Monster:
    name = '大黄'
    age = 3

    def hi(self):
        print(self.name, self.age)

    @staticmethod
    def ok():
        print('ok()....')

m = Monster()
m.ok()  #实例对象调用
# 不需要实例化，通过类即可调用静态方法
Monster.ok() #类对象调用