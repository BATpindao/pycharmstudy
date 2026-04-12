"""
daemon (守护进程)：一种“依附于主进程存在的子进程”，一旦主进程结束，他就会被自动终止。简言之主进程一死，守护进程必跟着死
使用场景：
1.后台监控类任务
2.日志/统计/采样 类任务
3.辅助型 “陪跑任务”

注意点：
1.守护进程必须是子进程
2.守护进程中，不允许在创建新的子进程
3.守护进程中，不允许再创建新的子进程
4.必须在start之前，start()之后，不能再设置daemon
"""
import os, time
from multiprocessing import Process


# python只有 全局作用域，和函数作用域，
"""
👉 Python：没有块级作用域，只有函数作用域
👉 所以 try / except 里的变量，外面也能用（前提是执行过）
"""

def monitor():
    while True:
        try:
            with open('/Users/apple/pandas_excel/log.txt', 'r', encoding='utf-8') as f:
                lines = sum(1 for _ in f)
        except FileNotFoundError as e:
            lines = 0
            print('文件还未创建')
        print(f'我是【守护进程】{os.getpid()}, 当前日志行数是：{lines}')
        time.sleep(1)

def test():
    for i in range(20):
        print(f'我是test：{os.getpid()},父进程:{os.getppid()}')
        time.sleep(1)

if __name__ == '__main__':
    print(f'我是主进程，进程id是：{os.getpid()}')
    p = Process(target=monitor)
    p2 = Process(target=test)
    p.start()
    p.daemon = True
    p2.start()

    with open('/Users/apple/pandas_excel/log.txt', 'a', encoding='utf-8') as f:
        for i in range(5):
            f.write(f'hello, {i}\n')
            f.flush()
            time.sleep(1)

    print('主进程结束')


