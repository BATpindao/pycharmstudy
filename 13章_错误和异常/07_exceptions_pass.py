"""
异常的传递：
    1.如果一个异常发生了，但是没有捕获处理异常，那么这个异常会传递给调用者处理
    2.如果所有的调用者都没有处理，最终会由系统处理
"""
def f3():
    print('----stat--f3()----')
    print(10/0)
    print('----end--f3()----')

def f2():
    print('----stat--f2()----')
    f3()
    print('----end--f2()----')

def f1():
    try:
        print('----stat--f1()----')
        f2()
        print('----end--f1()----')
    except Exception as e:
        print(f'f1()消息：{e},类型{e.__class__.__name__}')

f1()
