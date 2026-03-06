"""
模版设计模式
传统方法
"""

import time

class AA:
    def job(self):
        # 记录开始时间⌚️
        starter = time.time()
        print('程序开始执行')
        count = 0
        for i in range(1, 1001):
            count += 1
        end = time.time()
        print(f'程序执行结束，用时:{end - starter}')


class BB:
    def job(self):
        star = time.time()
        print('程序开始执行')
        count = 0
        for i in range(1, 1001):
            count += 1
        end = time.time()
        print(f'程序执行结束，用时:{end - star}')


if __name__ == "__main__":
    a = AA()
    a.job()