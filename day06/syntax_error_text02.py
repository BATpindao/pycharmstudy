"""
1.错误和异常练习题 进阶题

def safe_input():
要求：
。用户必须输入 整数
。输入错误 自动重新输入
。返回正确数字
使用：
。num = safe_input()
。print(num)
"""
from itertools import count


def safe_input() -> int:
    while True:
        try:
            num = int(input('请输入数字：'))
            return num
        except ValueError:
            print('输入错误，请重新输入')


def safe_div(a: int, b: int):
    try:
        if b == 0:
            raise ZeroDivisionError('除数不能为0')
        else:
            return a / b
    except ZeroDivisionError:
        print('除数不能为0，请重新输入')


# num = safe_input()
# print(num)

# print(safe_div(2,1))

"""
写一个函数：
    login()
要求：
    。用户输入用户名密码
    。错误 3 次就抛异常
    。正确则登录成功
例如：
    用户名：admin
    密码：123
    登录失败
三次后：
    Exception: 登录失败次数过多
"""


class LoginError(Exception):
    pass

def login():
    for i in range(3):
        user = input('输入用户名：')
        password = input('输入密码：')
        if user == 'admin' and password == '123':
            print('登录成功')
            return
        print('登录失败')
    raise LoginError('登录失败次数过多')


# 异常在函数里面抛出，在外面调用的时候就要捕获
try:
    login()
except LoginError as e:
    print(e)

