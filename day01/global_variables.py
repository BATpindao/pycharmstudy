# 函数的全局变量和局部变量练习
"""
题目1：基本区分全局和局部变量（简单）

描述：编写一个函数 print_vars()，
在函数内定义一个局部变量 local_x = 10，然后打印它。同时，在函数外定义一个全局变量 global_y = 20，
在函数内和函数外分别打印 global_y。观察局部变量是否能在函数外访问。

要求：
    1.不要修改全局变量。
    2.处理尝试访问局部变量时的错误（用 try-except）。
"""
global_y = 20


def print_vars():
    local_x = 10
    print('局部函数：', local_x)
    print('全局函数：', global_y)


print_vars()
print('全局函数：', global_y)

# try:
#     print('局部变量：',local_x)
# except NameError as e:
#     print(e)

print('第二题---------------------------------')
"""
题目2：修改全局变量（中等）

描述：定义一个全局变量 counter = 0。编写一个函数 increment_counter()，
在函数内使用 global 关键字将 counter 加 1，然后打印函数内和函数外的 counter 值。
调用函数两次，观察变化。

要求：如果不使用 global，会发生什么？（尝试后注释掉，改用 global）。
输出每次调用后的值。
"""

counter = 0


def increment_counter():
    # 想要修改全局变量的话，要先申明一下，才能改
    global counter
    counter += 1
    # counter = 1
    print('全局变量：', counter)


increment_counter()
print('第一次调用，全局变量：', counter)

increment_counter()
print('第二次调用，全局变量：', counter)

print("第三题：----------------------------")
"""
题目3：变量遮蔽（shadowing）（中等）
描述：定义全局变量 var = "global"。在函数 shadow_var() 内定义同名局部变量 var = "local"，
然后在函数内打印 var。函数外也打印 var。再添加一个内层函数（嵌套），在内层打印 var，观察哪个被使用。

要求：使用嵌套函数展示 LEGB 规则。
不要修改全局。
"""
var = "global"


def shadow_var():
    var = "local"

    def inner():
        print("内层函数:", var)  # 这里会用哪个？

    inner()
    print("函数内:", var)


shadow_var()
print("函数外:", var)

"""
题目4：使用 nonlocal 修改嵌套作用域（中等）
描述：编写一个外层函数 outer()，定义局部变量 num = 5。在内层函数 inner() 中，
使用 nonlocal 将 num 乘以 2。调用内层函数后，在外层打印 num。如果不使用 nonlocal，会发生什么？
要求：处理空列表或单个元素。
输出修改前后值。
"""


# 斐波那契数列
def fbn(i):
    if i == 1 or i == 2:
        return 1
    # 如果n>2，则对对应的斐波那契数列为 n-1 和 n-2对应的斐波那契数列的和
    else:
        return fbn(i - 1) + fbn(i - 2)


print('斐波那契数列：', fbn(7))

"""
2、猴子吃桃子问题:有一堆桃子，猴子第一天吃了其中的一半，并再多吃了一个!以后每天猴子都吃其中的一半，
然后再多吃一个。当到第10天时，想再吃时(即还没吃)，发现只有1个桃子了。
问题:最初共多少个桃子?
"""
def monkey(i):
    if i == 10:
        return 1
    else:
        return (monkey(i+1)+1)*2

print('猴子吃桃问题：',monkey(1))


print('===========================================================\n')
# 汉诺塔练习

def hanoi(num,a,b,c):
    """
    :param num: 制定盘子数
    :param a: A柱
    :param b: B柱
    :param c: C柱
    :return:
    """
    if(num==1):
        print(f'第一个盘子从：{a} -> {c}')
    else:
        # 如果有多个盘子，就分为两个部分，上面所有的盘和最下面的盘
        # 从A柱子上移动所有的上部分的盘子到B柱子，这个过程会借助到C柱子
        hanoi(num-1,a,c,b)
        # 移动最下面的盘
        print(f'第{num}个从：{a} -> {c}')
        # 把上面所有的盘从B柱子移动到C柱子，这个过程会使用到A柱子
        hanoi(num-1,b,a,c)

hanoi(3,'a','b','c')