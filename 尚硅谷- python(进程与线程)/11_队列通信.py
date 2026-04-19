"""
队列通信 queue

想要进程之间进行通信：可以使用 Queue(队列进行通信)
备注：q是在主进程中创建的，但可以被子进程使用，因为multiprocessing.Queue是跨进程的
为什么数据不会乱掉？————应为队列是先进先出的
"""
import os,time
from multiprocessing import Queue,Process

# 子进程1:在队列中接收数据
def test1(q):
    for i in range(5):
        print(f'进程：{os.getpid()}，正在接收消息：{q.get()}')
        time.sleep(1)

# 子进程2:在队列中发送数据
def test2(q):
    for i in range(5):
        print(f'进程：{os.getpid()}，正在发送消息：{i}')
        q.put(i)
        time.sleep(1)

if __name__ == '__main__':
    print(f'父进程：{os.getpid()}，启动')
    q = Queue()

    p1 = Process(target=test1,args=(q,))
    p2 = Process(target=test2, args=(q,))

    p2.start()
    p1.start()

    p2.join()
    p1.join()

    print(f'父进程：{os.getpid()}，结束')