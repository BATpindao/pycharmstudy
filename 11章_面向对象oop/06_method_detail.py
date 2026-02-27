"""
类中的成员方式的一些使用细节：
python也支持对象动态的添加方法
"""

def hi():
    print('hi python')

class Person:
    name = None
    age = None

    def ok(self):
        pass

# 创建对象 p1 p2
p1 = Person()
p2 = p1

"""
这里你调用了 hi() 函数，而 hi() 函数的作用是输出 hi python，所以它的返回值是 None，你实际上将 None 赋值给了 p1.hello。
然后，在你尝试执行 p1.hello() 时，会报错，因为 None 不能被调用。
正确的做法是，将 hi 函数本身赋给 p1.hello，而不是调用它。也就是说，
应该写成:p1.hello = hi 
"""
p1.hello = hi
p1.hello()

"""
1. 动态的给p1对象添加方法hello, 注意只是针对p1对象添加方法
2. hello是你新增加的方法的名称，由程序员指定名字
3. 即hello方法和函数hi关联起来, 当调用hello方法时，会执行hi函数
"""
print(type(p1.hello),type(hi),type(p1.ok))

# 应为hello没有动态的传递给 p2 所以这里执行会失败 如果这么写的话就可以 p2 = p1
p2.hello()


"""
重点小细节：
函数赋值的话后面不要加()，加了()的话就是将这个函数的返回值赋值给他

在 Python 中，你只能通过类名来实例化对象，比如 p1 = Person()，这时 Person 是类，你可以通过它来创建实例。
但如果你已经将 p1 赋值为一个 Person 类的实例，那么 p1 变成了一个对象，不能再作为类来调用了。
"""