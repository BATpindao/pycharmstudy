"""
抽象方法，模版设计
"""
import time
from abc import ABC, abstractmethod


class Templater(ABC):

    @abstractmethod
    def job(self):
        pass

    def time_j(self):
        print('程序开始执行')
        star = time.time()
        self.job()
        end = time.time()
        print(f'程序执行结束，耗时：{end - star}s')

class AA(Templater):
    def job(self):
        count = 0
        for i in range(1,1001):
            count += 1
            # print(i)

class BB(Templater):
    def job(self):
        count = 0
        for i in range(1,1001):
            count += 1
            print(i- count)

if __name__ == '__main__':
    a1 = AA()
    a1.time_j()