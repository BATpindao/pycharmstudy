"""
题目 1：不可变对象重新赋值
写函数 increment(x)，内部 x += 1，返回 x。
    .调用：a = 10；result = increment(a)；打印 a 和 result。
    .观察外部 a 是否变化。
"""

def increment(x):
    x += 1
    return x

a = 10
result = increment(a)
print(f'内存地址：{id(a)}',a) # a = 10
print(f'内存地址：{id(result)}',result) # result = 11 +=：这里其实是创建了一个新的值赋给了 x 内存地址变了


print()
"""
题目 2：可变对象就地修改
写函数 add_item(lst, item)，内部 lst.append(item)。
    .调用：my_list = [1, 2]；add_item(my_list, 3)；打印 my_list。
    .观察是否变化。
"""
def add_item(lst,item):
    lst.append(item)

my_list = [1,2]
add_item(my_list, 3)
print(my_list) # my_list 是一个可变对象 也没有用 = ，所以他的内存地址是没有变得


print()
"""
题目 3：可变对象重新赋值
写函数 replace_list(lst)，内部 lst = [4, 5, 6]。

调用：my_list = [1, 2, 3]；replace_list(my_list)；打印 my_list。
观察是否变化。
"""
def replace_list(lst):
    lst = [4,5,6]

my_list = [1,2,3]
replace_list(my_list)
print(my_list) # [1, 2, 3]  因为他用 = 这相当于是创建了一个新的列表赋给 lst 内存地址就变了 重新赋值不影响外部


print()
"""
题目 4：混合操作
写函数 mixed(lst, x)：

lst.append(100)
x = x + 10
返回 (lst, x)
调用：my_list = [1]；num = 5；new_lst, new_num = mixed(my_list, num)；打印所有变量。
"""
def mixed(lst, x):
    lst.append(x)
    x = x + 10
    return (lst, x)

my_list = [1]
num = 5
new_lst, new_num = mixed(my_list, num) #拆包
print(new_lst) #[1,5]
print(new_num) # 15


print()
"""
题目 5：默认参数陷阱
先写“有问题”的函数 append_one(lst=[])：lst.append(1) 并返回 lst。

调用三次 append_one()，观察输出（会共享！）。
然后修复它（用 None），再测试三次。
"""

def append_one(lst=[]):
    lst.append(1)
    return lst

def append_two(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst

print(append_one())
print(append_one())
print(append_one()) # 多次调用 lst 内存会连续共享

print(append_two())
print(append_two())
print(append_two()) # 这个每次调用的话都会创建一个新的 list 列表


print()
"""
题目 6：元组含可变对象（稍难）
定义 t = ([1, 2], "hello")

尝试 t[0].append(3)（合法？）
尝试 t[1] = "world"（报错？）
尝试 t = ([4, 5], "hi")（合法？）
打印最终 t。
"""
t = ([1,2],'helo')
t[0].append(3) # 合法 因为[1,2]是一个可变对象，用append不会改变其内存地址
# t[1] = "world" # 报错 应为 t[1]是一个不可变对象 ，= 这样的话是重新赋值 内存地址变了 这就改变了元组
t = ([4,5],'hi') # 不会 重新赋值了一个新的元组给 t ,而不是修改元组
print(t)