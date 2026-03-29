from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print(f'子进程 {name},{os.getpid()} 运行开始')


"""
在python中写通用 多进 程服务：
1.由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
2.multiprocessing模块提供了一个Process类来代表一个进程对象
语法：
    引入multiprocessing模块中的 Process类
    Process():创建一个新的子进程对象
    参数：target=指定子进程要执行的目标函数  ，args:传递给目标函数的参数元组
    参数详解：
    target：
        1.作用：指定子进程启动后要运行的函数
        2.类型：函数对象（不要加括号 ()）
    args：
        1.作用：传递给 target 函数的参数
        2.类型：必须是元组（tuple）
            。即使只有 1 个参数，也要加逗号 , 构成元组
            。如果没有参数，用空元组 args=()
            
1️⃣ p.start() - 启动子进程
作用：
    真正启动子进程
    操作系统创建新进程
    自动执行 target 指定的函数（如 run_proc('test')）
2️⃣ p.join() - 等待子进程结束
作用：
    阻塞主进程，等待子进程完成后再继续
    确保主进程不会在子进程结束前退出
    两种用法：
    ① p.join() - 无限期等待
    实例：
        p.start()
        p.join()  # 主进程停在这里，直到子进程结束
        print('所有进程结束')  # 子进程完成后才执行
    ② p.join(timeout=5) - 最多等待指定秒数
    实例：
        p.start()
        p.join(timeout=5)  # 最多等 5 秒，超时后主进程继续

"""
if __name__=='__main__':
    print(f'父类进程：{os.getpid()}')

    p = Process(target=run_proc, args=('test',))
    print('子类进程开始运行')
    #
    p.start()
    # p.join()意思是等待子进程结束
    p.join()

    print('子类进程运行结束')

"""
1.创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
2.join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

p = Process(target = 函数名,args = (传给函数的名))
"""