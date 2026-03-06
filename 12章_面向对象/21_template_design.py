"""
抽象方法，模版设计：

1.模版方法模式(templater method pattern) 经常和python抽象类 (abc) 一起使用，是面向对象里非常经典的设计模式
核心思想就一句话：
    父类定义算法骨架(流程)，子类只负责实现其中的具体步骤
这样做的好处：
    1.统一流程
    2.子类只关心差异
    3.避免重复代码

2.模版方法模式的结构：
    1.抽象类：定义整体流程
    2.模版方法(templater method)：固定算法步骤
    3.抽象步骤：子类必须实现
    4.可选步骤(hook)：子类可以重写
抽象类
│
├─ 模板方法（固定流程）
│      │
│      ├─ step1()
│      ├─ step2()  ← 子类实现
│      └─ step3()
│
└─ 子类
       └─ 实现具体步骤
"""
import time
from abc import ABC, abstractmethod


# 抽象类
class Templater(ABC):

    # 抽象步骤
    @abstractmethod
    def job(self):
        pass

    # 模版方法
    def time_j(self):
        print('程序开始执行')
        star = time.time()
        self.job()
        end = time.time()
        print(f'程序执行结束，耗时：{end - star}s')


class AA(Templater):
    def job(self):
        count = 0
        for i in range(1, 1001):
            count += 1
            # print(i)


class BB(Templater):
    def job(self):
        count = 0
        for i in range(1, 1001):
            count += 1
            print(i - count)


if __name__ == '__main__':
    a1 = AA()
    a1.time_j()
