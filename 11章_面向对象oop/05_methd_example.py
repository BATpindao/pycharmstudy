"""
成员方法的定义和使用：
.成员方法的定义：
    在类中定义成员方法和前面学习过的定义函数基本上一样(原理和运行机制是一样的)，但是还是有一点不一样(形式上有不同)
    定义成员方法的基本语法：
    def 方法名(self,行参列表)：
        方法体
解读：
1.在方法定义的参数列表中，有一个self
2.self是定义成员方法时，需要写上的
3.self表示对象本身
4.当我们通过对象调用方法时，self会隐试传入
5.在方法内部，需要使用self，才能使用成员变量
"""

"""
定义一个Person 类(name,age), 完成如下要求:
1) 添加hi 成员方法,输出 "hi, python"
2) 添加cal01 成员方法,可以计算从 1+..+1000的结果
3) 添加cal02 成员方法,该方法可以接收一个数n，计算从 1+..+n 的结果
4) 添加get_sum成员方法,可以计算两个数的和, 并返回
"""
class Person:
    name = None
    age = None

    def hi(self):
        print('hi,python')

    def cal01(self):
        j = 0
        for i in range(1,1001):
            j+=i
        print(j)

    def cal02(self,n):
        j = 0
        for i in range(1,n+1):
            j+=i
        print(j)

    def get_sum(self,a,b):
        return a+b

# 通过 对象.方法名 才能访问成员方法
p = Person()
p.hi()
p.cal01()
p.cal02(10)
print(p.get_sum(1,2))

