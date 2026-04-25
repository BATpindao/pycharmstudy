"""
ProcessPoolExecutor 进程池：
使用进程池的优势：如何使用进程池统一管理多个子进程，避免频繁 创建 / 销毁进程带来的开销，应为进程池会提前创建固定数量的进程，反复使用他们来执行任务
"""
# from concurrent.futures import ProcessPoolExecutor
# import os,time
#
# def work(n):
#     print(f'进程:{os.getpid()},接收值：{n}')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     print('主进程开始运行。。。。。')
#     # 创建一个进程池执行器
#     pool = ProcessPoolExecutor(3)
#
#     # 使用 submit 方法提交任务 (submit 只负责“提交任务”，不会阻塞主进程)
#     pool.submit(work,1)
#     pool.submit(work, 2)
#     pool.submit(work, 3)
#     pool.submit(work, 4)
#     pool.submit(work, 5)
#     pool.submit(work, 6)
#     pool.submit(work, 7)
#
#     # shutdown 的作用：不再接收新的任务
#     # wait=True 的作用：阻塞主进程，等待进程池中的任务全部执行完毕 默认是：false
#     pool.shutdown(wait=True)
#     print('主进程运行结束。。。。。')


# 获取子进程执行后的返回结果（future类的实例对象 + result方法）
from concurrent.futures import ProcessPoolExecutor
import os,time

def work(i):
    print(f'我正在执行任务：{i}。。。。。。进程：{os.getpid()}')
    time.sleep(1)
    return f'w我是任务{i}的结果'

if __name__=="__main__":
    print('我是主进程')

    pool = ProcessPoolExecutor(3)

    # submit不会堵塞主进程，是异步执行的，submit只负责执行提交任务
    # p1 = pool.submit(work,1)
    # p2 = pool.submit(work, 2)
    # p3 = pool.submit(work, 3)
    # p4 = pool.submit(work, 4)
    # p5 = pool.submit(work, 5)
    # p6 = pool.submit(work, 6)
    # p7 = pool.submit(work, 7)

    futures = [pool.submit(work,index) for index in range(1,8)]


    # 相当于multiprocessing 里的 process.join()放回阻塞主进程
    pool.shutdown(wait=True)

    for f in futures:
        print(f.result())
    # result() 会阻塞进程，等待结果返回才会执行后面的代码
    # print(p1.result())
    # print(p2.result())
    # print(p3.result())
    # print(p4.result())
    # print(p5.result())
    # print(p6.result())
    # print(p7.result())

    print('主进程执行结束')