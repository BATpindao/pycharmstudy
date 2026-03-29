from multiprocessing import Process
import time

def child():
    for i in range(3):
        print(f'子进程 {i}')
        time.sleep(0.5)

if __name__ == '__main__':
    p = Process(target=child)
    p.start()
    # 没有 join()
    # p.join()
    print('主进程结束')  # ⚠️ 可能子进程还没运行完，主进程就退出了
