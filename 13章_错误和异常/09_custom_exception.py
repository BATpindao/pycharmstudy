"""
自定义异常：
    1.程序可以通过创建新的异常类命名自己的异常，不论是直接还是间接的方式，异常都应该从Exception类派生
    2.异常类通常应当保持简单，它往往只提供一些属性，允许相应的异常处理程序提取有关错误的信息
    3.大多数异常类都以error结尾，类似标准的异常命名，但是需要注意不要使用内置异常名

实例题：
    当我们接收Person年龄时，要求范围在 18 – 120 之间，否则抛出一个自定义异常，并给出提示信息(循环提示,直到输入了正确的年龄)
"""


class AgeError(Exception):
    pass


while True:
    try:
        age = int(input('请输入年龄：'))
        if not(18 < age < 120):
            raise AgeError('请输入符合要求的年龄')

        print('年龄符合要求')
        break
    except ValueError as e:
        print('请输入正确的年龄')
    except AgeError as e:
        print(e)
    except Exception as e:
        print(e)
