"""
2.常见的异常实例演示
"""
# 1.IndexError: 当序列抽取超出范围时将被引发，也就是索引错误
str1 = 'hello word'
# print(str1[100])
list_str= ['jek','tom','king','luc','jec']
# print(list_str[5]) # IndexError: list index out of range 取值超出索引

# 2.keyError:当在现有键集合中找不到指定的映射（字典）键时将会被引发
my_dist = {'name':'jec','age':18,'sex':'男'}
# print(my_dist['school'])

# 3.NameError:当某个局部或全局名称未找到时将被引发，比如你使用了一个没有定义的变量名
# print(name)

# 4.TypeError:当一个操作或函数使用了类型不适当的对象时将被引发
a = 'qwe'
b = 1
# print(a+b)

# 5.ValueError:当操作或函数收到具有正确类型但值不适合的参数时将会被引发
# print(int('qwe'))

# 6.ZeroDivisionError:当除法和取余时第二个参数为零时将被引发
# print(10/0)

# 7.FileNotFoundError:请求的文件和目录不存在时将会被引发
# f = open('text.txt')

# 8.AttributeError:当属性引用或赋值失败时将被引发

class A:
    pass

a1 = A()
# print(a1.name) #AttributeError: 'A' object has no attribute 'name' 解释 A对象中没有name属性
