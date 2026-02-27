# 斐波拉数
def fbl(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fbl(n - 1) + fbl(n - 2)


print(fbl(3))

"""
猴子吃桃问题：有一堆桃子，猴子第一天吃了其中的一半，并在多吃了一个。
以后每天猴子都吃其中的一半，然后再多吃一个。当到第 10 天时，想再吃时（即还没吃），
发现只有 1 个桃子了。问最初共多少个桃子？
"""


def monkey(day, tao):
    if day == 1:
        return tao
    number = (tao + 1) * 2
    return monkey(day - 1, number)


result = monkey(10, 1)
print("最初桃子数：", result)

"""
求函数值，已知 f(1) = 3; f(n)= 2*f(n-1)+1；请使用递归的思想，求出 f(n)的值？
"""


def f(n):
    if n == 1:
        return 3
    else:
        return 2 * f(n - 1) + 1


print(f(10))


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