"""
join方法：
.作用：阻塞当前进程（通常是主进程），值到调用join的那个进程执行案必
.参数：join(timeout),timeout为超时时间（秒）,如果时间到了进程还没有结束，主进程就不等了，会继续执行
.注意：join 必须在 start() 之后调用
"""
import os,time
from multiprocessing import Process

def speak():
    for i in range(1,11):
        print(f'说话进程：{os.getpid()}，父进程：{os.getppid()}，name:{i}')
        time.sleep(1)

def study():
    for i in range(1,16):
        print(f'学习进程：{os.getpid()}，父进程：{os.getppid()}，name:{i}')
        time.sleep(1)

if __name__ == '__main__':
    print(f'主进程：{os.getpid()}')
    p1 = Process(target=speak)
    p2 = Process(target=study)


    """
    start： 
    join：阻塞进程，等待调用join的进程(线程)执行完成，后续的在执行
    """
    p1.start()

    # 让主进程等 p1 5秒钟 解释让主进程等待 p1 5秒之后，主进程继续执行后续的代码
    p1.join(5)
    p2.start()

    # p2.join() 让主进程等 p2 进程执行完毕后，主进程在继续执行
    p2.join()

    print('主进程结束')