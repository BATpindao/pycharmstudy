# GIL锁和编码时使用的 Lock 和 Rlock 不是同一个东西。
# Lock 和 Rlock是业务层面的锁，目标是：让业务逻辑别出错
# Rlock示例1：让打印是完整的
import time
from threading import Thread,RLock,current_thread

# def show_name1(lock):
#     for i in range(1,10):
#         with lock:
#             print("尚",end='')
#             print("硅", end='')
#             print("谷")
#         time.sleep(1)
#
# def show_name2(lock):
#     for i in range(1,10):
#         with lock:
#             print("黑",end='')
#             print("马")
#         time.sleep(1)
#
# if __name__ == '__main__':
#     lock = RLock()
#     t1 = Thread(target=show_name1,args=(lock,))
#     t2 = Thread(target=show_name2,args=(lock,))
#
#     t1.start()
#     t2.start()

# Rlock示例2：不要让两个窗口卖出同一张票 不加锁就会出现同一个窗口买同一张票
current = 1

def sale(lock):
    global current
    while True:
        with lock:
            if current <=20:
                print(f'{current_thread().name}出售了第：{current} 票')
                current+=1
            else:
                print('票已卖完')
                break
            time.sleep(1)

if __name__ == "__main__":
    lock = RLock()
    t1 = Thread(target=sale ,name='窗口1',args=(lock,))
    t2 = Thread(target=sale, name='窗口2',args=(lock,))
    t3 = Thread(target=sale, name='窗口3',args=(lock,))

    t1.start()
    t2.start()
    t3.start()