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
# from concurrent.futures import ProcessPoolExecutor
# import os,time
#
# def work(i):
#     print(f'我正在执行任务：{i}。。。。。。进程：{os.getpid()}')
#     time.sleep(1)
#     return f'w我是任务{i}的结果'
#
# if __name__=="__main__":
#     print('我是主进程')
#
#     pool = ProcessPoolExecutor(3)
#
#     # submit不会堵塞主进程，是异步执行的，submit只负责执行提交任务
#     # p1 = pool.submit(work,1)
#     # p2 = pool.submit(work, 2)
#     # p3 = pool.submit(work, 3)
#     # p4 = pool.submit(work, 4)
#     # p5 = pool.submit(work, 5)
#     # p6 = pool.submit(work, 6)
#     # p7 = pool.submit(work, 7)
#
#     futures = [pool.submit(work,index) for index in range(1,8)]
#
#
#     # 相当于multiprocessing 里的 process.join()放回阻塞主进程
#     pool.shutdown(wait=True)
#
#     for f in futures:
#         print(f.result())
#     # result() 会阻塞进程，等待结果返回才会执行后面的代码
#     # print(p1.result())
#     # print(p2.result())
#     # print(p3.result())
#     # print(p4.result())
#     # print(p5.result())
#     # print(p6.result())
#     # print(p7.result())
#
#     print('主进程执行结束')


# 3.使用as_completed():按”完成顺序“获取结果
# import os, time
# from concurrent.futures import ProcessPoolExecutor, as_completed
#
#
# def work(n):
#     print(f'任务{n}正在执行任务。。。。{os.getpid()}')
#     if n == 1:
#         time.sleep(10)
#     elif n == 2:
#         time.sleep(5)
#     else:
#         time.sleep(1)
#     return f'这是程序：{n} 的执行结果'
#
#
# if __name__ == '__main__':
#     print('-----start------')
#     # 创建一个进程池执行器
#     completed = ProcessPoolExecutor(3)
#
#     # 使用submit 方法提交任务 （submit 只负责提交任务 不会阻塞主进程）
#     futures = [completed.submit(work, index) for index in range(1, 8)]
#     # 准备一个 result_list 去收集任务的具体结果
#     results_list = []
#     # 收集每个任务的结果
#     for i in as_completed(futures):
#         results_list.append(i.result())
#     # 阻塞主进程，等待进程池中所有任务执行完毕
#     completed.shutdown(wait=True)
#     # 打印最终的结果
#     print(results_list)
#     print('--------end---------')

# 4.使用add_done_callback 方法 ,为任务添加一个完成时候的回调函数
# import os,time
# from concurrent.futures import ProcessPoolExecutor
#
# def work(n):
#     print(f'任务{n}正在执行任务。。。。{os.getpid()}')
#     if n == 1:
#         time.sleep(10)
#     elif n == 2:
#         time.sleep(5)
#     else:
#         time.sleep(1)
#     return f'这是程序：{n} 的执行结果'
#
# if __name__ == '__main__':
#     print('------start--------')
#     p = ProcessPoolExecutor(3)
#
#     result_list = []
#     # 任务完成后的回调函数
#     def callback_func(future):
#         result_list.append(future.result())
#
#     # 开启7个任务并指定,回调函数
#     for i in range(1,8):
#        #  submit()方法 会返回一个future对象
#        p_result = p.submit(work,i)
#        p_result.add_done_callback(callback_func)
#
#     p.shutdown(wait=True)
#     print(result_list)
#
#     print('----------end---------')

# 5.使用map方法批量提交任务(注意: map方法本身不阻塞,但读取其返回的生成器对象是阻塞的,并且的到结果的顺序,与任务分配的任务是一致的)
# import os, time
# from concurrent.futures import ProcessPoolExecutor
#
#
# def work(n):
#     print(f'任务{n}正在执行任务。。。。{os.getpid()}')
#     if n == 1:
#         time.sleep(10)
#     elif n == 2:
#         time.sleep(5)
#     else:
#         time.sleep(1)
#     return f'这是程序：{n} 的执行结果'
#
#
# if __name__ == '__main__':
#     print('------start------')
#     # 创建啊一个进程执行器
#     executor = ProcessPoolExecutor(3)
#
#     # 通过 map 方法批量提交任务 (结果按照提交的顺序来)
#     results = executor.map(work, [1, 2, 3, 4, 5, 6, 7])
#     # 获取results里生成器里面的内容
#     print(list(results))
#     # 等待所有任务都完成
#     executor.shutdown(wait=True)
#     print('--------end---------')

# 6.使用with: 进程池的"自动回收" 写法.离开 with 代码快就会自动执行 shutdown(wait=True)
from concurrent.futures import ProcessPoolExecutor
import os,time

def work(n):
    print(f'任务{n}正在执行任务。。。。{os.getpid()}')
    if n == 1:
        time.sleep(10)
    elif n == 2:
        time.sleep(5)
    else:
        time.sleep(1)
    return f'这是程序：{n} 的执行结果'

if __name__ == '__main__':
    print('-----start-------')
    p = ProcessPoolExecutor(3)
    with p as a:
      results = a.map(work,[1,2,3,4,5,6,7])
      print(list(results))
    # 这里会自动执行等待所有进程完成

    print('-----end-------')