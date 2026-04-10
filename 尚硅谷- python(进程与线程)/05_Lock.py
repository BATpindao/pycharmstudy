import os, time
from multiprocessing import Process, Lock, RLock


def spek(lock):
    for i in range(1, 11):
        # 上锁：如果锁是空闲的，立刻上锁，继续往下执行；如果锁被别人拿着：当前进程会阻塞等待
        lock.acquire()
        lock.acquire()
        print('AA', end='')
        print('BB', end='')
        print('CC', end='')
        print('DD')
        time.sleep(1)
        # 释放锁：acquire 和 release 必须成对出现，否则会永远卡住（死等）
        lock.release()
        lock.release()


def study(lock):
    for i in range(1, 16):
        # with lock: 会自动完成两件事：
        #   (1).进入前：自动执行 lock.acquire() 上锁
        #   (2).离开后：自动执行 lock.release() 释放锁
        # 好处是：即便代码块里发生异常，也能保证释放锁，避免“卡死”
        with lock:
            print('好好', end='')
            print('学习', end='')
            print('天天', end='')
            print('向上')
            time.sleep(1)


if __name__ == "__main__":
    print(f'我是主进程：{os.getpid()}')
    from multiprocessing import set_start_method

    set_start_method("fork")

    """
    传统的lock在面对多次上锁时，会产生死锁状态，解决办法就是用RLock（可重入锁）
    | 锁类型   | 特点          |
    | ----- | ----------- |
    | Lock  | 同一个进程不能重复上锁 |
    | RLock | 同一个进程可以重复上锁 (那几次锁，就要释放几次锁)|
    | 性能    | Lock稍快      |
    | 安全性   | RLock更安全    |

    """
    # 创建一个锁对象
    # lock = Lock() #用多锁的话这里就会变成死锁
    lock = RLock()  # 这个就不会死锁

    p1 = Process(target=spek, name='说话进程', args=(lock,))
    p2 = Process(target=study, args=(lock,))

    #
    p1.start()
    p2.start()

    print('进程运行结束')
