"""
python一切皆为对象，所有对象都有一个布尔值，通过内置函数bool()可以获取对象的布尔值
"""
print('布尔值：',bool(False))
print('数值:',bool(0))
print('空对象:',bool(None))
print('空字符串：',bool(''))
print('空列表：',bool([]))
print('空字典：',bool({}))
print('空元组：',bool(()))
print('空集合：',bool(set()))


# 判断 一下对象的值

s = '1'
if s :
    print(s)
else:
    print('是空值')