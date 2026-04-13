"""
队列(Queue)是一种“先进先出”的数据结构（先放进去的数据，一定会先取出来）
"""

import time
from multiprocessing import Process, Queue

# 创建一个队列（不限制大小，即：不设置容量上限）
q1 = Queue()

# 创建一个队列（最多能保存3个元素）
q2 = Queue(3)

# 1 put方法：往队列里放数据（入队）
# q2.put('10')
# q2.put('20')
# q2.put('30')

# 2 get方法：从队列里取数据（出队）
# print(q2.get())
# print(q2.get())
# print(q2.get())

# 3.empty方法：判断队列是否为空 （这个方法在多线程的情况下不准确）
# print(q1.empty())

# 4.full判断队列是否已满
# q2.put('10')
# q2.put('20')
# q2.put('30')
# print(q2.full())

# qzise方法：获取队列的长度
# q2.put(10)
# q2.put(20)
# q2.put(30)
# print(q2.qsize())

# 6.队列具备等待模式
# q2.put(40)
# q2.put(50)
# q2.put(60)

# (1)当队列已满时，继续put,就会进入等待模式，等别人调用get方法，取走一个元素，才能继续添加
# q2.get()
# q2.put(70)
# print('放入完毕')

# (2)当队列已满时，执行 put(元素,timeout = 秒数) ，就会等待指定的时间，如果规定时间内没有put成功,则会报错
# q2.put(80, timeout=2)

# (3).put_nowait()方法，会直接向队列添加元素，不会进入等待模式，如队列已满，则会报错
# 备注：put_nowait()方法，等价于put(元素,blok=False),blok默认是 True
# block：当队列已满时，程序会阻塞等待，直到有空位可以放入数据
# q2.put_nowait(400)
# q2.put(200,block=False)

# get 读多了也会进入等待模式
# q1.get()
# q1.get()
# q1.get()

# (1)当队列已空时，继续get,就会进入等待模式，等别人调用put方法，添加一个元素，才能继续取
# q2.get()

# (2)当队列已空时，执行 get(timeout = 秒数) ，就会等待指定的时间，如果规定时间内没有get成功,则会报错
# q2.get(timeout=3)

# (3)get_nowait()方法，会直接从队列中读取元素，不会进入等待模式，若队列已空，则会报错
q2.put(100)

print(q2.get_nowait())
