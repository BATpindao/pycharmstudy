def f1(index):
    print('sum01')
    print('sum02')
    print('sum03')
    sum1 = f2(index)
    print('sum05')
    print('sum06')
    print('sum07')


def f2(index):
    for i in range(index):
        print('循环次数：',i)
    print('END!')
    return i


f1(10)

"""
Step Over F8 逐行执行
step into F7 进入方法内部
step out 跳出方法内部
"""
