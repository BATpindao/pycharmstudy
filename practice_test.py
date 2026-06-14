import asyncio

async def work():
    print('work开始工作')
    print('work执行中。。')
    print('work结束工作')
    return '工作结果'


coroutine_retuen = work()

retule = asyncio.run(coroutine_retuen)

print(retule)