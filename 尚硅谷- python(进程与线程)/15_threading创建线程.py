import os, time
from multiprocessing import Process, RLock
from threading import get_native_id,Thread,RLock

def spek(lock):
    for i in range(1,6):
        with lock:
            print(f'我是说话进程:{i},进程是:{os.getpid()},线程id:{get_native_id()}')
        time.sleep(1)

def study(lock):
    for i in range(1,6):
        with lock:
            print(f'我是学习进程:{i},进程是:{os.getpid()},线程id:{get_native_id()}')
        time.sleep(1)

if __name__ == '__main__':
    print(f'我是主进程：{os.getpid()},主线程是:{get_native_id()}')
    # Thread 的参数：
    # 🔸group： 默认值为 None（应当始终为 None）。
    # 🔸target： 子线程要执行的可调用对象，默认值为 None。
    # 🔸name： 线程名称，默认为 None。如果设置为 None，Python 会自动分配名字
    # 🔸args： 给 target 传的位置参数（元组）。
    # 🔸kwargs： 给 target 传的关键字参数（字典）。
    # 🔸daemon： 标记线程是否为守护线程，取值为布尔值（默认为 None）。
    # 使用 Thread 创建线程对象
    lock = RLock()
    t1 = Thread(target=spek,args=(lock,))
    t2 = Thread(target=study,args=(lock,))

    #调用线程对象的start方法，会立刻将该线程交由系统进行调度
    t1.start()
    t2.start()

    # 让主线程等 t1和t2 线程执行完毕后，主线程再继续执行。
    t1.join()
    t2.join()
    print('主进程运行结束')
#这运行的代码就有 主进程，主进程里面有三个线程，一个主线程，两个字线程

"""
使用 Thread 创建线程
1.任何一个正在运行的python程序，至少多有一个线程！

if __name__ == '__main__':
    print('主进程中的代码')
对于上述代码来，：print('主进程中的代码')确实属于主进程，但跟准确的说，是运行在主进程里的 “主线程中”

2.线程是进程里面的执行单位：
    .一个进程里，至少有一个线程（主线程）
    .一个进程里，可以有多个线程
    .多个线程之间会：共享进程里的内存空间，但执行顺序由操作系统调度
"""
