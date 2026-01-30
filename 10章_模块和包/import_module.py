"""
模块的导入：
    1.基本语法：
        [from 模块名(文件名字)] import (函数｜类｜变量名｜*) [as 别名]
        解读：
            []里面的东西是可选的
            可以更具需求，选择合适的形式引入
"""

# import math
# import random
#
# print('返回一个绝对值：',math.fabs(-111.12))
# print('从列表中随机返回一个元素：',random.choice(['air pos max','mac','iphone']))

"""
2.导入一个或多个模块:
    语法：
        import 模块
        import 模块1，模块2
    建议：
        1.导入多个模块时，还是一行导入一个模块
        2.使用 模块.xx 方式来使用相关的功能、.表示层级关系、几模块中的xx (函数|类|变量名|*)
        3.import 语句 通常写在文件开头
"""
# import math,random
# print('绝对值：',math.fabs(-111),'随机值：',random.choice(['iphone','mac','air']))


"""
3.导入模块的的指定功能：
    语法：
    form 模块 import 函数、类、变量..
    使用：
        因为导入了具体函数、类、变量、直接使用即可、不需要再带模块名
"""
# from math import fabs
# from random import choice
# print('绝对值：',fabs(-21))
# print('随机数：',choice(range(1,11)))

"""
4.导入模块的全部功能
    form 模块名 import *
    讲解：
        直接使用，不需要带 模块名
"""
# from math import *
# print('求绝对值：',fabs(-33))
# print('求平方根：',sqrt(9))

"""
5.给导入的 模块 或 功能 取别名
    语法：
        import 模块名 as 别名
        from 模块名 import 函｜数类｜变量.. as 别名
    解读：
        1.import 模块 as 别名 ：给导入的模块取别名，使用：被名.xx
        2.from 模块 import 函数 类 变量.. as 别名 ：给导入的摸个功能取被名，使用时直接用别名即可
"""

import math as mt
from random import choice as c

print('绝对值：',mt.fabs(-333))
print('随机数：',c(['air','ipo','iphone']))