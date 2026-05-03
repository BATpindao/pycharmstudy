# 线程池
import os,time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor,as_completed
from threading import get_native_id,RLock


# 1️⃣创建『线程池执行器』、使用 submit 方法提交任务、使用 shutdown 方法等待任务完成。
# def work(n,lock):
#     with lock:
#         print(f'{n}正在工作.......{get_native_id()}')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     print('------------start--------------')
#     # 创建线程池
#     t = ThreadPoolExecutor(3)
#
#     l =  RLock()
#     # 创建线程池 使用submit 方法提交任务
#     t.submit(work,1,l)
#     t.submit(work, 2, l)
#     t.submit(work, 3, l)
#     t.submit(work, 4, l)
#     t.submit(work, 5, l)
#     t.submit(work, 6, l)
#     t.submit(work, 7, l)
#
#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     t.shutdown(wait=True)
#     print('------------end--------------')

# 2️⃣获取子线程执行后的返回结果（Future类的实例对象 + result方法）
# def work(n,lock):
#     with lock:
#         print(f'{n}正在工作.......{get_native_id()}')
#     time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('------------start--------------')
#     # 创建线程池
#     t = ThreadPoolExecutor(3)
#
#     l =  RLock()
#     # 创建线程池 使用submit 方法提交任务
#     futers = [t.submit(work,index,l) for index in range(1,8)]
#
#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     t.shutdown(wait=True)
#
#     for i in futers:
#         print(i.result())
#     print('------------end--------------')

# 3️⃣使用 as_completed：按“完成顺序”获取结果

# def work(n,lock):
#
#     with lock:
#         print(f'{n}正在工作.......{get_native_id()}')
#     time.sleep(1)
#     if n ==1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('------start------')
#     t = ThreadPoolExecutor(3)
#     lock = RLock()
#
#     futures = [t.submit(work,index,lock) for index in range(1,8)]
#
#     result_list = []
#     # 收集每个任务的结果
#     for i in as_completed(futures):
#         result_list.append(i.result())
#
#     t.shutdown(wait=True)
#
#     print(result_list)
#
#     print('------end------')

# 4️⃣使用 add_done_callback 方法，为任务添加完成时的回调函数
# def work(n,lock):
#
#     with lock:
#         print(f'{n}正在工作.......{get_native_id()}')
#     time.sleep(1)
#     if n ==1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('------start------')
#     t = ThreadPoolExecutor(3)
#     lock = RLock()
#
#     result_list = []
#
#     def add_callback(f):
#         result_list.append(f.result())
#
#     for i in range(1,8):
#         t1 = t.submit(work,i,lock)
#         t1.add_done_callback(add_callback)
#
#     t.shutdown(wait=True)
#
#     print(result_list)
#
#     print('------end------')

# 5️⃣使用 map 方法批量提交任务（注意：map方法本身不阻塞，但读取其返回的生成器对象是阻塞的，并且得到结果的顺序，与任务分配的顺序是一致的）
# def work(n,lock):
#
#     with lock:
#         print(f'{n}正在工作.......{get_native_id()}')
#     time.sleep(1)
#     if n ==1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('------start------')
#     t = ThreadPoolExecutor(3)
#     lock = RLock()
#
#     t_map = t.map(work,[1,2,3,4,5,6,7],[lock]*7)
#     print(list(t_map))
#
#     t.shutdown(wait=True)
#
#     print('------end------')

# 6️⃣使用 with：线程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
def work(n,lock):
    with lock:
        print(f'{n}正在工作.......{get_native_id()}')
    time.sleep(1)
    if n ==1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    return f'任务{n}的结果'

if __name__ == '__main__':
    print('------start------')

    with ThreadPoolExecutor(3) as t:
        lock = RLock()
        t_map = t.map(work,[1,2,3,4,5,6,7],[lock]*7)
        print(list(t_map))


    print('------end------')