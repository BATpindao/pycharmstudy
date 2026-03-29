"""
pool:
    1.pool是multiprocessing模块下的一个类
    2.如果要启动大量的子进程，可以用进程池的方式批量创建子进程
"""
"""
模块讲解：
Pool:进程池类
os:获取进程ID
random：生成随机数
time:获取程序运行时间
"""
from multiprocessing import Pool
import os, random, time


def loog_time_task(name):
    print(f'任务启动 {name}--{os.getpid()}')
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print(f'任务：{name} 运行了：{end - start:.2f}秒')

if __name__ == '__main__':
    # 显示主进程ID
    print(f'父进程： {os.getpid()}')

    # 创建进程池
    p = Pool(4)

    for i in range(5):
        # apply_async：异步非阻塞方式
        p.apply_async(loog_time_task, args=(i,))
    #这会立即执行（因为apply_async不阻塞）
    print('等待所有子进程完成....')

    # 关闭进程池，停止添加新的进程，已提交的任务会继续执行完成
    p.close()

    # 阻塞主进程，等待所有子进程完成，必须在close()之后调用
    p.join()
    print('所有子流程完成....')

"""
运行结果：
父进程： 2902
等待所有子进程完成....
任务启动 0--2907
任务启动 1--2906
任务启动 2--2904
任务启动 3--2905
任务：2 运行了：1.29秒
任务启动 4--2904
任务：4 运行了：0.78秒
任务：1 运行了：2.35秒
任务：3 运行了：2.52秒
任务：0 运行了：2.93秒
所有子流程完成....

解读：
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
调用close()之后就不能继续添加新的Process了。

请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
这是因为Pool的默认大小，因此，最多同时执行4个进程。这是Pool有意设计的限制，
并不是操作系统的限制。

由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
"""