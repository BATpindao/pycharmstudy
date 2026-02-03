"""
对象的传递机制： 对象是一个可变类型
"""

class Person:
    name = None
    age = None

p1 = Person()

p1.name = '小明'
p1.age = 20

# p1赋值给了p2，即让p2的内存地址指向p1
p2 = p1
print(p2.name)
print('内存地址：',id(p1),id(p2))

print()
a = Person()
a.name = 'tom'
a.age =12

b = a
print(b.name)
b.age = 22
b = None #注意这里 b 的指向变了 ， a的没有变
print(b.name) #报错，因为此时b的指向是None 里面没有name的属性
print(a.name,a.age) #tom 22