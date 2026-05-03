import time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

def cpu_task(n):
    print(f'任务：{n}开始了')
    with open('java.zip','rb') as read_zip , open(f'java_{n}副本.zip',"wb") as with_zip:
        while True:
            data = read_zip.read(1024*1024)
            if not data:
                break
            with_zip.write(data)

if __name__=='__main__':
    # print('======多进程完成cpu密集型任务==========')
    # start = time.time()
    #
    # with ProcessPoolExecutor(4) as p:
    #    for i in range(1,5):
    #        p.submit(cpu_task,i)
    #
    # end = time.time()-start
    #
    # print(f'多进程耗时：{end}')
    print('======多线程完成cpu密集型任务==========')
    start = time.time()

    with ThreadPoolExecutor(4) as p:
       for i in range(1,5):
           p.submit(cpu_task,i)

    end = time.time()-start

    print(f'多线程耗时：{end}')

