"""
1.isinstance() 用于判断对象是否为某个类或其子类的对象
2.基本语法：isinstance(object，classinfo)
参数解读：
    object：对象
    classinfo：可以是类名，基本类型或者由他们组成的元组
"""

class AA:
    pass
class BB(AA):
    pass
class CC:
    pass

aa = AA()
bb = BB()

print('aa 是不是 AA 的对象(或是其子类)',isinstance(aa, AA))
print('bb 是不是 AA 的对象(或是其子类)',isinstance(bb, AA))
print('aa 是不是 CC 的对象(或是其子类)',isinstance(aa, CC))

# int类型

num = 8

print('num 是不是 int 的对象(或是其子类)',isinstance(num, int))
print('num 是不是 int 的对象(或是其子类)',isinstance(num, str))

# 元组的使用，只要是其中任何一个就可以
print('num 是不是 int 的对象(或是其子类)',isinstance(num, (int, str)))