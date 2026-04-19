"""
继承Process 创建多进程：
当子进程逻辑比较复杂，或者想把【进程 + 行为】封装成一个整体时，可以使用继承Process类的方法去创建进程，这种方法属于“面向对象”

1.核心要点：
。必须继承Process类
。把子进程要干的事，写进 run() 方法
。依然使用 stater() 方法启动进程，不要手动调用 run()！
。若子进程不需要参数，可以不写 __init__，若需要参数，则需要写 __init__
。传给的子进程的参数，作为实例属性保存
"""
import time,os
from multiprocessing import Process,Lock

class SpeakProcess(Process):
    def __init__(self,a,lock:Lock):
        super().__init__()
        self.a = a
        self.lock = lock

    def run(self):
        for i in range(5):
            with self.lock:
                print(f'进程 {os.getpid()} 正在说话...,接收的值：{self.a}')
                time.sleep(1)

class StudyProcess(Process):
    def run(self):
        for i in range(5):
            print(f'进程 {os.getpid()} 正在学习...')
            time.sleep(1)

if __name__ == '__main__':
    from multiprocessing import set_start_method
    set_start_method("fork")

    print(f'主进程：{os.getpid()}，启动')

    l = Lock()
    s1 = SpeakProcess(12,l)
    s2 = StudyProcess()

    s1.start()
    s2.start()

    s1.join()
    s2.join()

    print(f'主进程：{os.getpid()}，结束')