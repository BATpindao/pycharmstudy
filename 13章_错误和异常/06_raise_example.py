"""
raise语句支持强制触发指定的异常
"""

try:
    num1 = 10
    num2 = 0
    res = num1 +num2
    # 支持强制异常触发
    raise ZeroDivisionError('除数不能为0')
except ZeroDivisionError as e:
    print(f'异常信息{e},异常类型{type(e)}')