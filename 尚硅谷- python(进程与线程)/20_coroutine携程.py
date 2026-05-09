# coroutine 协程
import asyncio

"""
协程对象和协程函数：
协程函数（coroutineFunction）：使用「async关键字」修饰的函数，就是协程函数
协程对象（coroutineObject）：调用「协程函数」就会得到「协程对象」

"""

# 注意⚠️：调用『协程函数』，并不会执行『协程函数』中的代码
async def work():
    print('work开始。。。。')
    print('work执行。')
    print('work结束。。。。')
    return '工作结果'

# 调用协程函数，就会得到协程对象
coroutine_object = work()

# asyncio.run 方法做了三件事情：
#   1.创建一个时间循环
#   2.将收到的携程对象，包装成一个任务（task），交给事件循环
#   3.启动时间循环
# 注意⚠️asyncio.run 会阻塞当前线程，知道任务执行结束，return的最终结果
result = asyncio.run(coroutine_object)

print(result)