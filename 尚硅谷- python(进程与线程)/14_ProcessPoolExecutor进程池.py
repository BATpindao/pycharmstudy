"""
ProcessPoolExecutor 进程池：
使用进程池的优势：如何使用进程池统一管理多个子进程，避免频繁 创建 / 销毁进程带来的开销，应为进程池会提前创建固定数量的进程，反复使用他们来执行任务
"""
from concurrent.futures import ProcessPoolExecutor
import os,time

def work(n):
    print(f'进程:{os.getpid()},接收值：{n}')
    time.sleep(1)

if __name__ == '__main__':
    print('主进程开始运行。。。。。')
    # 创建一个进程池执行器
    pool = ProcessPoolExecutor(3)

    # 使用 submit 方法提交任务 (submit 只负责“提交任务”，不会阻塞主进程)
    pool.submit(work,1)
    pool.submit(work, 2)
    pool.submit(work, 3)
    pool.submit(work, 4)
    pool.submit(work, 5)
    pool.submit(work, 6)
    pool.submit(work, 7)

    # shutdown 的作用：不再接收新的任务
    # wait=True 的作用：阻塞主进程，等待进程池中的任务全部执行完毕 默认是：false
    pool.shutdown(wait=True)
    print('主进程运行结束。。。。。')