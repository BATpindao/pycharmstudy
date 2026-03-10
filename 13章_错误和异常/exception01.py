"""
捕获异常：
如果想要程序在发生异常后还可以继续执行，就要用异常捕获
对异常进行捕获，保证可以继续执行
"""
# 捕获异常，进行处理，这样程序可以再出现异常的情况下，继续执行
#
try:
    num1 = 10
    num2 = 0
    print(num1/num2)
except Exception as e:
    # 当我们得到异常后（捕获异常），程序员自己处理
    # 可以在这里做一些处理
    """
    解读：
    e.__class__:在 Python 中，每个对象都有一个 __class__ 属性，表示它属于哪个类
    e.__class__.__name__: __name__ 是类对象的名字，也就是类名本身的字符串。
    就是显示异常的类的名字
    """
    print(f'捕获异常，异常是{e.__class__.__name__}')
print('程序员继续执行。。。')

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