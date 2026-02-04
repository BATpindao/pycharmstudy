"""
属性/成员变量、类变量、成员变量
1.类中定义的属性(变量)，我们也称为成员变量
2.属性是类的一个组成部分，一般是字符串，数值，也可以是其他类型(list,dict等)，还可以是类

注意事项和细节说明：
1.属性的定义语法同变量，示例：属性名 = 值 ，如果没有值，可以复制为None
None解读：
1.None是python的内置常量，通常被用来代表空值对象

"""
class Cat:
    # cat ,name,color 属性 类变量
    age = None
    name = None
    color = None
    weight = None
    pass

# 通过cat类 创建 实力(示例对象/对象)
cat1 = Cat()
# 通过 对象名.属性名  可以给各个属性赋值
cat1.age = 2
cat1.name = '咪咪'
cat1.color = 'wait'
cat1.weight = 15
print(id(cat1))
# 通过 对象名.属性名 可以访问到属性
print(f'第一只喵咪的信息:名字-{cat1.name}，年龄：{cat1.age}，颜色：{cat1.color}，体重：{cat1.weight}')


"""
对象的传递机制： 对象是一个可变类型
"""

class Person:
    name = None
    age = None

a = Person()
a.name = 'tom'
a.age =12

b = a
print(b.name)
b.age = 22
b = None #注意这里 b 的指向变了 ， a的没有变
print(b.name) #报错，因为此时b的指向是None 里面没有name的属性
print(a.name,a.age) #tom 22