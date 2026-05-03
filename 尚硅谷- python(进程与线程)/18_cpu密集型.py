import time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

def cpu_task(n):
    print(f'任务：{n}开始了')
    i= 0
    for index in range(10000000):
        i+=index
    return i

if __name__=='__main__':
    # print('======多进程完成cpu密集型任务==========')
    # start = time.time()
    #
    # with ProcessPoolExecutor(4) as p:
    #    cpu_list = list(p.map(cpu_task,[1,2,3,4]))
    #
    # end = time.time()-start
    #
    # print(f'多进程耗时：{end}')
    # print(cpu_list)

    print('======多线程完成cpu密集型任务==========')
    start = time.time()

    with ThreadPoolExecutor(4) as p:
       cpu_list = list(p.map(cpu_task,[1,2,3,4]))

    end = time.time()-start

    print(f'多线程耗时：{end}')
    print(cpu_list)