"""
5.异常处理：
基本介绍：
    异常处理就是当异常发生的时，对异常处理的方式
异常捕获的语法：
try:
    可能出现异常的代码
except[异常 as 别名]:
    发生异常时，对异常处理的代码
else:
    没有发生异常，执行的代码
finally:
    不管有没有异常，都要执行的代码
"""
try:
    num1 = 10
    num2 = 0
    # res = num1 / num2
    res = num1 + num2
except (ZeroDivisionError,ValueError,KeyError) as e:
    print('除数不能为0')
except Exception as e:
    print(f'铺后的异常信息：{e} ,异常的类型：{type(e)}')
else:
    print('没有异常执行')
finally:
    print('不论有没有异常都要执行')

print('程序继续执行..')

"""
使用细节（注意事项）：
    1.如果异常发生了，则异常发生后面的代码不会执行，直接进入到except字句里
    2.如果异常没有发生，则顺序执行try的代码块，不会进入except字句
    3.如果希望没有发生异常，要执行某段代码，则使用else字句
    4.如果希望不管有没有发生异常，都要执行某段代码(比如关闭链接，释放资源等)则使用finally字句
    5.可以有多个except字句，捕获不同的异常(进行不同的业务处理)，如果发生异常，则只会匹配一个except，建议把具体的异常写在前面，
    基类写在后面，这样匹配不到时，再由基类匹配（兜底）
    6.一个except字句，也可以捕获不同的异常
"""