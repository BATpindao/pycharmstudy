# 练习 函数参数的练习

"""
题目 1：简单默认参数（热身）
写一个函数 introduce(name, age=18, city="Beijing")，打印介绍信息："我是{name}，今年{age}岁，来自{city}。"
要求：
1.测试几种调用方式：全位置、全关键字、混用、只提供部分参数。

思路提示：直接用默认值。注意调用时位置实参必须在关键字实参前。
"""

def introduce(name, age=18, city="Beijing"):
    print(f'我是{name},今年{age}岁，来自{city}')

introduce('anna',21,'newyouk')
introduce(name='京王',age=12,city="Beijing")
introduce('三',age=31,city="Beijing")
introduce('明')


print()
"""
题目 2：可变位置参数 *args
写一个函数 average(*numbers)，计算并返回所有传入数字的平均值（如果没有数字，返回 0）。
要求：

测试：average(1, 2, 3) → 2.0；average() → 0；average(10) → 10。

思路提示：*numbers 收集成 tuple，用 sum(numbers) / len(numbers) 计算（注意 len==0 的情况）。
"""
def average(*numbers):
    # print(type(numbers),numbers,len(numbers))
    if len(numbers) == 0:
         return 0
    else:
        return sum(numbers) / len(numbers)

print(average(1,2,3))
print(average())
print(average(10))


print()
"""
题目 3：可变关键字参数 **kwargs
写一个函数 print_person_info(name, **kwargs)，先打印名字，然后打印其他信息（如 age、job、hobby 等）。
要求：

调用示例：print_person_info("Alice", age=25, job="Engineer", hobby="Reading")
输出格式：每行一个 "key: value"

思路提示：**kwargs 是 dict，用 for 循环遍历 items() 打印。
"""
def print_person_info(name, **kwargs):
    print(name)
    for key,value in kwargs.items():
        print(f'{key}={value}')

print_person_info(name="Alice", age=25, job="Engineer", hobby="Reading")

print()
"""
题目 4：混合参数 + 仅关键字参数（中等）
写一个函数 create_profile(name, age, *, city, job="Student", **hobbies)：
name 和 age 是普通参数。
city 是必填的仅关键字参数。
job 是可选仅关键字默认参数。
**hobbies 收集其他关键字（如 hobby1="reading", hobby2="swimming"）。

要求：
测试几种调用，观察哪些会报错。
打印所有信息。
思路提示：用 * 分隔仅关键字参数。调用时 city 必须用关键字传。
"""
def create_profile(name,age,*,city,job='student',**hobbies):
    print(name,age,city,job,hobbies)

create_profile('tom',12,city="Beijing",hobby="reading",add="4034邮政")
create_profile('tim',43,city='newyouk') # City，job 要传值给这两个参数，只能用关键字传参，不然会报错：他只需要两个位置参数，但是传了三个
create_profile(name='tom',age=18,city="Beijing",hobby="reading")#如果第一个位置用了关键字传参，后面也要用关键字传参


print()
"""
题目 5：参数解包（中等偏难）
写一个函数 sum_three(a, b, c)，返回 a+b+c。
要求：

用列表 [1, 2, 3] 和字典 {'a': 10, 'b': 20, 'c': 30} 通过解包调用它。
再写一个支持任意个数相加的版本，用 *args。
思路提示：调用时用 *list 解包位置，**dict 解包关键字。
"""

def sum_three(a,b,c):
    return a+b+c

sum_list = [1,2,3]
print(sum_three(*sum_list))

sum_dict = {'a':10, 'b':20, 'c':30}
print(sum_three(**sum_dict))

# 补充：任意个数相加版本
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all())              # 0
print(sum_all(10, 20))

print()
"""
题目 6：默认参数陷阱 + 修复（稍难）
先写一个“有问题”的函数 add_item(item, lst=[])：把 item 添加到 lst 并返回 lst。
测试多次调用 add_item(1)、add_item(2)，观察输出（会共享列表！）。
然后修复它，让每次调用都用新列表（除非显式传入 lst）。
思路提示：经典陷阱。用 lst=None，然后 if lst is None: lst = []。
"""
# def add_item(item,lst=[]):
#     lst.append(item)
#     return lst
#
# print(add_item(1))
# print(add_item(2))
# print(add_item(3,lst=[]))
# lst 是一个可变参数

def add_item(item,lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
print(add_item(3))
print(add_item(4,[]))