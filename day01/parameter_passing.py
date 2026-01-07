"""
函数作为参数传递
1.练习
"""


# 比较两个值之间的最大值
def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val


def f1(fun, num1, num2):
    """
    功能：调用fun返回num1和num2的最大值
    :param fun: 表示接收一个函数
    :param num1: 传入一个数
    :param num2: 传入一个数
    :return: 返回最大值
    """
    return fun(num1, num2)


def f2(fun, num1, num2):
    """
    功能：调用fun返回num1和num2的最大值
    :param fun: 表示接收一个函数
    :param num1: 传入一个数
    :param num2: 传入一个数
    :return: 返回最大值
    """
    return num1 + num2, fun(num1, num2)


print(f1(get_max_val, 10, 20))
print(f2(get_max_val, 10, 20))
x, y = f2(get_max_val, 10, 20)
print(x, y)

print('----------传多个函数')
# 一个函数可以接受多个函数作为参数，注意作为参数的函数，
def f3(my_fun, num1, num2,my_fun2):
    return my_fun(num1, num2),my_fun2(num1, num2)


# 定一个函数，可以返回两个数的和
def get_sum(num1, num2):
    return num1 + num2

print(f3(get_max_val,100,200,get_sum))
