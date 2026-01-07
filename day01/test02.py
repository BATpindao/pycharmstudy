# 递归函数

# 乘机 n!
def factorial(n):
    """
    递归就是要无限靠近 基线条件
    :param n:
    :return:
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print('求乘机 n!:', factorial(5))


# 遍历列表求和
def sum_list(list):
    # 基线条件
    if len(list) == 1:
        return list[0]
    else:
        # 递减
        return list[0] + sum_list(list[1:])


print('列表求和：', sum_list([1, 2, 3, 4]))


# 反转字符串 hello olleh
def reverse_string(s):
    # len(s)==1 这是基准数
    if len(s) == 1:
        return s[0]
    else:
        # reverse_string(s[1:]) 这其实是取出下一个的字符串
        return reverse_string(s[1:]) + s[0]


print('反转字符串：', reverse_string('hello'))


# 计算幂 power(2,3) return: 8

def power(number, exp):
    if exp == 1:
        return number
    else:
        return number * power(number, exp - 1)


print('计算幂直：', power(3, 3))

"""
检查会文。 回文是从前往后读是一样的，从后往前读也是一样的 aba asa
忽律大小写
"""


def is_palindrome(num):
    num = str(num).replace(" ", "")
    if len(num) >= 2:
        if num[0].lower() == num[-1].lower():
            return True if is_palindrome(num[1:-1]) is True else False
        else:
            return False
    else:
        return True


print('判断是不是会文：', is_palindrome('A man a plan a canal Panama'))

"""
汉诺塔问题（稍难）：写一个函数 hanoi(n, from_rod, to_rod, aux_rod)，
打印移动 n 个盘子从 from_rod 到 to_rod 的步骤（用 aux_rod 作为辅助）。经典问题，n=3 时应该输出移动序列。
"""


def hanoi(n, from_rod='A', to_rod='C', aux_rod='B'):
    if n == 1:
        print(f"Move disk 1 from {from_rod} to {to_rod}")
        return
    hanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from {from_rod} to {to_rod}")
    hanoi(n - 1, aux_rod, to_rod, from_rod)


# 测试 n=3
hanoi(3)

"""
猴子吃桃问题：有一堆桃子，猴子第一天吃了其中的一半，并在多吃了一个。以后每天猴子都吃其中的一半，
然后再多吃一个。当到第 10 天时，想再吃时（即还没吃），发现只有 1 个桃子了。问最初共多少个桃子？
"""


# i是天数 返回的是桃子的数
def monkey1(i):
    if i == 10:
        return 1
    else:
        return (monkey1(i + 1) + 1) * 2


print(monkey1(1))

"""
求函数值，已知 f(1) = 3; f(n)= 2*f(n-1)+1；请使用递归的思想，求出 f(n)的值？
"""

def f(n):
    if n == 1:
        return 3
    else:
        return 2 * f(n - 1) + 1;

print(f(3))

"""

"""


