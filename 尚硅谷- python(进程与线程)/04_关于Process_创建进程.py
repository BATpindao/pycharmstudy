import time, os
from multiprocessing import Process,current_process

print(__name__, os.getpid())


def study(a,b,age):
    for i in range(1, 11):
        # current_process().name 在进程内部获取进程名称的名字
        print(f'学习进程，name:{i},{current_process().name},进程：{os.getpid()},父进程：{os.getppid()},{a,b,age}')
        time.sleep(1)


def speak():
    for i in range(1, 16):
        print(f'说话进程,name:{i},进程：{os.getpid()}，父进程：{os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':
    from multiprocessing import set_start_method
    set_start_method("fork")
    # 主进程
    print(f'主进程，进程：{os.getpid()}')
    """
    在实例化 Process 时，可以传递以下参数：
        🔸group： 默认值为None（应当始终为None）。
        🔸target：子进程要执行的可调用对象，默认值为 None。
        🔸name：  进程名称，默认为 None ，如果设置为 None，Python 会自动分配名字。
        🔸args：  给 target 传的位置参数（元组）
        🔸kwargs：给 target 传的关键字参数（字典）。
        🔸daemon：标记进程是否为守护进程，取值为布尔值（默认为 None，表示从创建方继承）。
    """
    p1 = Process(target=study, name='学习进程',args=(1,2),kwargs={'age':12})
    p2 = Process(target=speak)

    # 获取并打印两个子进程的名称
    print(p1.name, p2.name)

    p1.start()
    p2.start()
