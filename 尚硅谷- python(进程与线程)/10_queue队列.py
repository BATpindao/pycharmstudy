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
# print(q2.empty())

# 4.full判断队列是否已满
# q2.put('10')
# q2.put('20')
# q2.put('30')
# print(q2.full())

# qzise方法：获取队列的长度

print(q1.qsize())