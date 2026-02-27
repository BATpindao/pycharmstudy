# 课后练习
"""
题目 1：列表最大值（递归版）
用递归实现一个函数 find_max(lst)，返回列表 lst 中的最大值。
要求：
不能用内置的 max() 函数。
必须用递归（可以参考之前列表求和的思路）。
考虑空列表的情况（可以返回 None 或抛出提示，但既然你还没学异常，就返回 None 吧）。
"""


def max_value(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    else:
        return lists[0] if lists[0] > max_value(lists[1:]) else max_value(lists[1:])


print(max_value([-2, -3, -9]))

"""
题目 2：用 lambda 和 map/filter 实现字符串列表处理
有一个字符串列表 words = ["apple", "banana", "kiwi", "pear", "fig", "orange"]。
请分别用 lambda + map / filter 完成以下任务（可以写多个小表达式）：

得到所有长度大于 5 的水果名（返回新列表）。
得到所有水果名的大写版本（返回新列表）。
得到每个水果名的长度列表（如 [5, 6, 4, 4, 3, 6]）。

提示：记得用 list() 转换 map/filter 的结果。
"""
words = ['apple', 'banana', 'kiwi', 'pear', 'fig', 'orange']
# 获取长度大于5的水果名字
name_list = list(filter(lambda n: len(n) > 5, words))
print(name_list)

# 水果的大写名字
name_list_upper = list(map(lambda n: n.upper(), words))
print(name_list_upper)

# 获取每个水果名字的长度
name_leng = list(map(lambda n: len(n), words))
print(name_leng)

"""
题目 3：高阶函数 - 自定义计算器
写一个高阶函数 calculator(operation)，它接收一个 lambda 函数作为参数 operation，然后返回一个新函数，这个新函数接受两个数字并用传入的 operation 计算。
示例用法：
Python
add_calc = calculator(lambda x, y: x + y)
print(add_calc(10, 5))   # 输出 15

multiply_calc = calculator(lambda x, y: x * y)
print(multiply_calc(4, 7))  # 输出 28

power_calc = calculator(lambda x, y: x ** y)
print(power_calc(2, 8))   # 输出 256
"""

# 返回一个新的函数
# 接受一个lambda函数
def calculator(lmd):
    def new_fun(a,b):
        return lmd(a,b)
    return new_fun


add_calc = calculator(lambda x, y: x + y)
print(add_calc(10, 5))

multiply_calc = calculator(lambda x, y: x * y)
print(multiply_calc(4, 7))

power_calc = calculator(lambda x, y: x ** y)
print(power_calc(2, 8))

"""
题目 4：递归求列表中所有元素的乘积
用递归实现函数 product_list(lst)，返回列表中所有元素的乘积。
要求：

不能用内置函数。
处理空列表返回 1（乘法单位元），单个元素直接返回该元素。

示例：
Pythonprint(product_list([2, 3, 4]))   # 输出 24
print(product_list([5]))         # 输出 5
print(product_list([]))          # 输出 1
"""


def product_list(lst):
    if len(lst) == 0:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] * product_list(lst[1:])


print('递归函数：', product_list([5]))

"""
题目 5：结合 lambda 和 sorted 排序复杂列表
有一个学生成绩列表：
Pythonstudents = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
    {"name": "赵六", "score": 92}
] 
请用 sorted() 和 lambda 实现：

按成绩从高到低排序（分数相同按名字字母顺序排序）。
只返回名字列表，按成绩从高到低排列。

示例期望输出：

排序后列表：李四(92)、赵六(92)、张三(85)、王五(78)（名字顺序李四在前因为 L < Z）
名字列表：['李四', '赵六', '张三', '王五']

提示：sorted 的 key 可以是 lambda 返回元组，Python 会按元组顺序比较。
"""

students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
    {"name": "赵六", "score": 92}
]
#
i = sorted(students, key=lambda n : (-n['score'],n['name']))

print([(key['name'],key['score']) for key in i])