"""
进程通信：queue类
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
"""
from multiprocessing import Process,Queue
import os,time,random


# 队列写入数据
def write(e:Queue):
    print(f'进程：{os.getpid()} 开始向队列写入数据')
    for value in ['A','B','C']:
        print(f'向队列写入：{value}')
        e.put(value)
        time.sleep(random.randint(1,3))

def red(e:Queue):
    print(f"进程：{os.getpid()} 正在读取数据")
    while True:
        value = e.get(True)
        print(f'队列读取数据：{value}')

if __name__ == '__main__':
    # 父进程创建一个Queue(创建一个管道用于通信)，传递给各个子进程
    q = Queue()

    # 创建两个进程，一个写入，一个读取
    pw = Process(target=write, args=(q,))
    pr = Process(target=red, args=(q,))

    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()

    # 等待w写入数据完成
    pw.join()
    # 强制关闭读取进程，无法等待期结束，强制关闭
    pr.terminate()