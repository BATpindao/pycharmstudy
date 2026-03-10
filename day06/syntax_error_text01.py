# 十二、经典练习（非常重要）

"""
练习 1：不断输入数字，如果输入错误继续输入。

while True:
    try:
        num = int(input("请输入数字:"))
        print("你输入的是:", num)
        break

    except ValueError:
        print("输入错误，请输入数字")
"""
while True:
    try:
        number = int(input('请输入数字:'))
        print(10/number)
    except ValueError as e:
        print('请输入数字')
    except ZeroDivisionError as e:
        print('除数不能为0')
    else:
        break

"""
练习 2：
计算两个数除法。
要求：
输入不是数字提示
除数不能为 0
"""
try:
    num = int(input('请输入数字:'))
    print(10/num)
except ValueError:
    print('输入的不是数字')
except ZeroDivisionError:
    print('除数不能为0')
