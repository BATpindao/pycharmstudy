"""
课堂练习：
    如果用户输入的不是一个整数, 就提示他反复输入，直到输入一个整数为止
"""

while True:
    try:
        number = int(input('请输入一个整数:'))
        break
    except ValueError:
        print('你输入的不是一个整数')
    except Exception as e:
        print('你输入的不是一个整数',type(e))