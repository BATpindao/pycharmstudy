"""
函数作为参数传递

特性：
在 Python 中，函数是一等公民（first-class citizen），
这意味着函数可以像普通变量一样被
   赋值
   传递
   返回
1.接收函数作为参数的函数是一个高阶函数

基本语法：
def 高阶函数(普通函数, 数据):
    # 在这里调用 普通函数 处理 数据
    pass
"""
from turtledemo.penrose import start

# 练习 使用内置高阶函数
numbers = [1, 2, 3, 4]

# map: 把一个函数应用到数列的每一个元素中
squats = list(map(lambda x: x ** 2, numbers))
print('map-求numbers中每个元素2的乘机：', squats)

# filter:根据函数返回值（False/True）,筛选元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
print('filter-删选出numbers中的偶数：', evens)

# sorted 用key函数指定排序规则
words = ['apple-mac', 'huawei', 'xiaomi', 'mac studio']
sorted_by_len = list(sorted(words, key=len))
print('sorted-指定排序规则：', sorted_by_len)

"""
自定义高阶函数
"""


# 高阶函数
def apply_number(fun, a, b):
    # 函数处理
    return fun(a, b)


# 普通函数
def add_number(a, b):
    return a + b


def multiply(a, b):
    return a * b


# 调用
print('使用自定义函数：+:', apply_number(add_number, 2, 3))
print('使用自定义函数：*:', apply_number(multiply, 2, 3))

"""
=======================函数练习题========================
"""

"""
第一题： 写一个高阶函数 calculator(operation, x, y)，它接受一个运算函数 operation 和两个数字，返回运算结果。
要求：
实现加、减、乘、除四个函数（可以用 lambda 或 def）。
用 calculator 调用它们得到结果。
"""


def claculator(operation, x, y):
    """
    calculator：高阶函数
    :param operation: 普通函数
    :param x: 参数
    :param y: 参数
    :return: 返回值
    """
    return operation(x, y)


# 加
def add_number(x, y):
    return x + y


# 减
def j_number(x, y):
    return x - y


# 乘机
def multiply_number(x, y):
    return x * y


# 除数
def c_number(x, y):
    return x / y


print('+', claculator(add_number, 2, 3))
print('-', claculator(j_number, 2, 3))
print('*', claculator(multiply_number, 2, 3))
print('/', claculator(c_number, 2, 3))

"""
题目 2：列表变换
写一个函数 transform_list(func, lst)，它接受一个函数 func 和一个列表 lst，返回一个新列表，新列表的每个元素是 func 作用在原元素上的结果。
要求：

用它把 [1, 2, 3, 4] 变成平方列表、立方列表、负数列表。
"""
number_list = [1, 2, 3, 4]


def pf_func(key):
    return key ** 2


# 平方的计算
pf_number = [pf_func(itm) for itm in number_list]
print('求列表中元素的平方：', pf_number)

# 立方的计算
lf_number = list(map(lambda x: x ** 3, number_list))
print('求元素中的立方：', lf_number)

# 负数列表
fs_number = list(map(lambda x: 0 - x, number_list))
print("转化成负数：", fs_number)

"""
题目 3：自定义过滤
写一个函数 my_filter(condition, lst)，它接受一个返回布尔值的函数 condition 和一个列表，返回满足条件的元素组成的新列表。
要求：
用它从 [1, 2, 3, 4, 5, 6] 中筛选出所有偶数、所有大于 3 的数、所有能被 3 整除的数。 
提示这里要用 lambda函数
"""


def my_filter1(condition, list):
    # 列表推导式：只把 condition(item) 为 True 的 item 加入新列表
    return [item for item in list if condition(item)]


def my_list2(condition, list):
    number_list = []
    for item in list:
        if condition(item):
            number_list.append(item)
    return number_list


numbers = [9, 1, 2, 3, 4, 6]
print('方法一：筛选出所有的偶数：', my_filter1(lambda x: x % 2 == 0, numbers))
print('筛选出既大于3又能被3整除的数：', my_filter1(lambda x: x > 3 and x % 3 == 0, numbers))
print('方法二，筛选大于3的值：', my_list2(lambda x: x > 3, numbers))

"""
题目 4：排序灵活化
有一个学生列表，每个学生是字典：[{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 92}, ...]
写一个函数 sort_students(students, key_func)，根据 key_func 返回的值对学生列表排序（返回新列表）。
要求：
分别按分数升序、降序、名字字母顺序排序。
"""


def sort_students(students, key_func):
    return key_func(students)


# 升序
def key_func_s(students):
    return list(sorted(students, key=lambda stu: stu['score']))


# 降序
def key_fun_j(students):
    return list(sorted(students, key=lambda stu: -stu['score']))


# 名字字母排序
def key_sorted_name(students):
    return list(sorted(students, key=lambda student: student['name']))


students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Anna', 'score': 85},
    {'name': 'Bill', 'score': 92}
]

print('分数升序排序：', sort_students(students, key_func_s))
print('按分数降序排：', sort_students(students, key_fun_j))
print('安字母来排序：', sort_students(students, key_sorted_name))

"""
题目 5：组合函数（稍难）
写一个高阶函数 compose(f, g)，它返回一个新函数，新函数先对输入执行 g，再把结果传给 f 执行。
即：compose(f, g)(x) 等价于 f(g(x))
要求：

实现 add_one = lambda x: x + 1
square = lambda x: x * x
用 compose(square, add_one)(5) 得到 36（(5+1)^2）
"""


def compose(f, g):
    return lambda x: f(g(x))


add_one = lambda x: x + 1
square = lambda x: x * x

print('高阶函数：', compose(square, add_one)(5))

# 新的练习题
"""
题目 1：多次组合（简单热身）
写一个高阶函数 compose3(f, g, h)，它接受三个函数，返回一个新函数，新函数的执行顺序是：先 h(x) → 再 g(结果) → 再 f(结果)。
要求：

定义 add_one = lambda x: x + 1
multiply_two = lambda x: x * 2
square = lambda x: x * x
用 compose3(square, multiply_two, add_one)(5) 得到结果 144
（计算过程：5 → +1 → 6 → ×2 → 12 → 平方 → 144）
"""


def compose3(f, g, h):
    return lambda x: f(g(h(x)))


add_one = lambda x: x + 1
multiply_two = lambda x: x * 2
square = lambda x: x * x

print('多函数：', compose3(square, multiply_two, add_one)(5))

"""
写一个高阶函数 pipeline(funcs)，它接受一个函数列表 [f1, f2, f3, ...]，返回一个新函数，从左到右依次应用这些函数。
即：pipeline([f1, f2, f3])(x) 等价于 f3(f2(f1(x)))
要求：

用它实现：从 5 开始 → 加1 → 乘3 → 平方 → 得到 (5+1)*3 的平方 = 324
"""


# 这里要用递归函数+函数传参
def pipeline(funcs):
    if len(funcs) == 1:
        return funcs[0]
    else:
        return lambda x: funcs[0](pipeline(funcs[1:])(x))


list_lambda = [lambda x: x ** 2, lambda x: x * 3, lambda x: x + 1]

print('第二题：', pipeline(list_lambda)(5))

"""
题目 3：带参数的函数工厂（中等偏难）
写一个高阶函数 make_multiplier(n)，它接受一个数字 n，返回一个新函数，这个新函数会把输入乘以 n。
要求：
double = make_multiplier(2)
triple = make_multiplier(3)
打印 double(5) → 10，triple(5) → 15

思路提示：make_multiplier 返回一个 lambda，里面要“记住”参数 n（这涉及闭包）。返回 lambda x: x * n 即可。重点理解：返回的函数即使在 make_multiplier 执行完后，仍然能访问 n。
"""


def make_multiplier(n):
    return lambda x: x * n


double = make_multiplier(2)
triple = make_multiplier(3)
print('函数工厂：', double(5))
print('函数工厂：', triple(5))

"""
题目 4：简单装饰器入门（稍难，拓展）
写一个高阶函数 timer(func)（装饰器雏形），它接受一个函数 func，返回一个新函数，新函数会在调用原函数前后打印时间（模拟计时）。
要求：
用 import time
定义一个测试函数 slow_add(a, b)：先 sleep 1 秒，再返回 a + b
用 timed_add = timer(slow_add)
调用 timed_add(3, 4)，输出类似：text开始执行...
结果: 7
耗时: 约1.00秒
思路提示：
返回一个新函数（可以用 def 或 lambda），里面：
start = time.time()
result = func(*args, **kwargs)（要支持任意参数，所以用 *args, **kwargs）
end = time.time()
打印信息
return result
这些题目会让你更熟练地使用“返回函数”和“函数组合”。先从第1题开始试试，写完任意一道（或全部）贴代码给我，我会详细反馈！加油，你进步很快～🚀
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):           # 支持任意参数
        print("开始执行...")
        start = time.time()                 # 开始计时（调用时）
        result = func(*args, **kwargs)      # 执行原函数
        end = time.time()
        cost = end - start
        print(f"结果: {result}")
        print(f"耗时: 约{cost:.2f}秒")         # 保留两位小数
        return result                       # 可选：返回结果
    return wrapper                          # 返回新函数


def slow_add(a, b):
    time.sleep(1)                           # 模拟慢操作
    return a + b


# 使用
timed_add = timer(slow_add)
timed_add(3, 4)


