"""
python函数：参数绑定详解

python的参数绑定有四种方式：
按顺序绑定：
1.先绑定位置形参（从左到右）(位置参数)。
2.再绑定默认形参（如果没提供实参，用默认值）(默认参数)。
3.可变位置参数（*args）收集剩余位置实参  (可变位置参数)。
4.可变关键字参数（**kwargs）收集剩余关键字实参。 (可变关键字参数)
"""

# 1.位置参数的使用
"""
(1) 位置参数（Positional Parameters）
最简单：必须按顺序提供实参。
绑定方式：按位置从左到右匹配。
"""

def greet(name, age):
    print(f'你好{name},今年{age}')

greet('Anna', 23)
# greet('Anna')  #报缺少参数错误  TypeError: greet() missing 1 required positional argument: 'age'
# greet('anna',23,12)  #报错  参数 多余错误


# 2.关键字参数传参
"""
关键字参数（Keyword Arguments）

调用时用 形参名=值 的形式。
优点：顺序无关，可读性强；可以跳过默认参数。
"""
def student(name,age):
    print(f'同学名字:{name}，年龄:{age}')

student(name='Anna', age=23)
student(age=23,name='TIM') #关键子调用顺序可以随意写

# 3.默认参数
"""
默认参数（Default Arguments）
1.定义时指定默认值：def func(a, b=10):
2.默认值在函数定义时计算一次（重要陷阱！）。
3.调用时可省略，提供时覆盖默认值。
"""
def add(a,b=3):
    return a+b

print(add(1)) #4 (默认用 b=3)
print(add(1,2)) #3 (覆盖默认)

# 注意：经典的陷阱题：可变默认值共享
def bad_append(item,lst=[]):
    lst.append(item)
    return lst

print(bad_append(1)) #[1]
print(bad_append(2)) #[1,2]。← 共享了同一个列表
print(bad_append(3,[])) #[3] 提供了新的列表没问题

# 正确的写法
def bad_append2(item,lst=None):
    if lst is None:
        lst = []  #每次创建新列表
    lst.append(item)
    return lst

print(bad_append2(1)) #[1]
print(bad_append2(2)) #[2] ← 独立
print(bad_append2(3,[])) #[3] ← 独立


# 4.可变长参数
"""
3. 可变长参数（Variable-Length Arguments）
(1) *args：可变位置参数
1.收集多余的位置实参成 tuple。
2.名字通常叫 args，但可以自定义（如 *numbers）
"""
def sum_all(*args):
    print('args类型：',type(args))
    return sum(args)

print(sum_all(1,2,3)) #6
print(sum_all(1,2,3,4,5,6)) #16
print(sum_all()) #0(空 tuple)

# 混用
def func(a,b,*c):
    print(a,b,c)

func(1,2,3,4,5,6) #结果 1 2 (3,4,5,6)


# 5.可变关键字参数
"""
**kwargs：可变关键字参数
1.收集多余的关键字实参成 dict。
2.名字通常叫 kwargs。
"""
def print_info(**kwargs):
    print('kwargs 类型:',type(kwargs))
    for k,v in kwargs.items():
        print(f'{k},{v}')

print_info(name='Anna', age=23,city='biejin')
# 输出：
# kwargs 类型: <class 'dict'> 字典
# name,Anna
# age,23
# city,biejin

# 混用 位置参数 ，可变长参数，可变关键词参数

def func_hun(a,*b,**c):
    print(a,b,c)

func_hun(1,2,3,4,name='Anna',age=23,city='biejin') #结果：1 (2, 3, 4) {'name': 'Anna', 'age': 23, 'city': 'biejin'}


"""
参数定义顺序规则 （非常重要！）
python 严格要求形参顺序：
  def func(pos1, pos2, /, positional_or_keyword, *, keyword_only):
      pass
      
      完整顺序（从左到右）：
        1.位置或关键字参数（普通参数，可位置或关键字调用）。
        2./ 前：仅位置参数（Positional-Only，Python 3.8+，如内置函数 pow(x, y, /)）。
        3.默认参数（可省略）。
        4.*args（可变位置）。
        5.仅关键字参数（Keyword-Only：在 * 之后，无默认或有默认）。
        6.**kwargs（可变关键字）。
标准常见顺序：
def func(a, b=10, *args, c, d=20, **kwargs):  # c, d 是仅关键字（在 *args 后）
    ...

判断：顺序是否对：
func(1, 2, 3, 4, c=5, x=10)  # a=1(位置), b=2(位置), args=(3,4), c=5(必须关键字), kwargs={'x':10}
# func(1, 2, 3, 4, 5)  # 报错：c 缺少
"""

# 6参数解包 （UnpacKing）
"""
调用时可以用 * 和 ** 解包 序列 / 字典
"""
def add(x,y,z):
    return  x+y+z

numbers = [1,2,3]
print('列表解包参数：',add(*numbers)) # 6 --解包列表

info = {'x':22,'y':1,'z':3}
print('字典解包：',add(**info)) #26 -- 解包字典 （键名匹配行参名）


#6.综合示例

def complex_func(a,b=2,*args,c,d=4,**kwargs):
    """
     正确示例：
     - a,b: 普通位置/关键字参数 （b 有默认值）
     - *args： 收集多余的位置实參
     - c ,d 仅限关键字参数（c 必填，b  有默认值，必须用关键字传）
     - **kwargs: 收集多余的关键字实參
    """
    print(f'a={a},b={b},args={args},c={c},d={d},kwargs={kwargs}')

#正确调用示例
complex_func(1,c=2) #函数的位置参数使用： a=1,b=2,args=(),c=2,d=4,kwargs={}
complex_func(1,2,3,4,5,c=8,d=9) #a=1,b=2,args=(3, 4, 5),c=8,d=9,kwargs={}
complex_func(a=1,b=2,c=3,d=4) #a=1,b=2,args=(),c=3,d=4,kwargs={}

#错误示例
# complex_func(1,5,6) #报错：缺少必填的仅关键字参数 c
complex_func(1,b=6,c=1) ## 报错：位置实参不能出现在关键字实参后