"""
pipe 进程通信：
pipe 就像一根水管，一头负责发送，一头负责接收
"""
import os,time
from multiprocessing import Process,Pipe

# Pipe() 会返回两个对象，他们分别代表管道的两端 send()发送 ,recv()接收
# duplex用于控制管道为单向还是双向，true表示双向，false表示单向
# 单向 pipe 的规则：con1只能发送，con2只能接收
# con1 , con2 = Pipe(duplex = True) #创建--管道
# 单向 pipe 的规则：con1只能接收，con2只能发送
# 单向 Pipe 的规则 con1zhi

def test1(p):
    p.send(100)
    print(f'tesst1 发送数据成功 100')

    time.sleep(3)
    # data = p.recv()
    # print(f'tesst1 接收数据成功 {data}')

def test2(p):
    data = p.recv()
    print(f'tesst2 发送接收成功 {data}')

    # time.sleep(2)
    # p.send(200)
    # print(f'tesst1 发送数据成功 200')


if __name__ == '__main__':
    print(f'主进程开始:{os.getpid()}')
    """
    duplex:true 的话 con1,con2 是又可以接收数据，又可以发送消息
    duplex:false con1只能接收，con2只能发送
    """
    con1 , con2 = Pipe(duplex = False)
    p1 = Process(target=test1 ,args=(con2,))
    p2 = Process(target=test2,args=(con1,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'主进程结束:{os.getpid()}')