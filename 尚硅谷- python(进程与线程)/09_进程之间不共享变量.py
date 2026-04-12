from multiprocessing import Process

number = 100
names = []

def test1(number,names):
    # global number,names
    names.append('小王')
    number += 10
    print('子进程执行完毕，number1的值是：', number,names)

def test2(number,names):
    # global number, names
    names.append('王2')
    number -= 10
    print('子进程执行完毕，number2的值是：', number,names)

"""
进程之间不共享内存，因此也就不共享任何变量，不管变量是可变的还是不可变的，都不共享
，但是有些东西就是共享的，lock就是可以共享的
"""
if __name__ == '__main__':
    p1 = Process(target=test1,args=(number,names))
    p2 = Process(target=test2,args=(number,names))
    p1.start()
    p2.start()

    print(f'num的值是：{number,names}')