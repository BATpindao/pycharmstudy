"""
数据容器
主要：
    1.列表（list）     特性：有序、可变、允许重复元素、像一个可伸缩的数组
    2.字典 （dict）    特性：无序Python 3.7+ 插入顺序保留）、可变、键唯一（键必须不可变）。像一个键值映射表。 key=value
    3.字符串（string）  特性：
    4.元组 （tuple）   特性：有序、“不可变”、允许元素重复、像一个“只读”列表
    5.集合（set）。     特性：无序，可变，不允许元素重复、常用于去重和数学集合运算。
"""

# 列表 list --最常用、可变容器
"""
定义：用 [] 或 list()。 lst=[]
特点：有序（有索引，从0开始）、可变（增删改）、允许重复。
"""
# 创建一个 列表 list
my_list = [1, 2, 3, 2, 'hello', True, ['hello', 'word']]  # 混合类型也可以，可以存储多个类型的参数
empy_list = [4, 3, 7, 9]

# 切片/访问
print(my_list[0])  # 1  索引从0开始
print(my_list[-1])  # ['hello','word'] (负索引从末尾开始)
print(my_list[:3])  # [1, 2, 3]   切片访问是 包前不包后的
print(my_list[3:6])  # 。['hello', True, ['hello', 'word']]（切片，不包含末尾）

# 修改元素
my_list[0] = 100  # [100, 2, 3, 'hello', True, ['hello', 'word']]
# print('修改：', my_list)

# 添加
my_list.append(129)  # append 是末尾添加  [100, 2, 3, 'hello', True, ['hello', 'word'], 129]
my_list.extend([5, 6])  # 批量添加，添加的位置也是在末尾
# print('添加.append:', my_list)

# 插入
my_list.insert(2, '插入insert')  # 指定位置插入
# print('指定位置插入.insert', my_list)

# 删除
my_list.remove('hello')  # 删除第一个屁配置
del my_list[-1]  # 删除指定索引

popped = my_list.pop()  # 删除并返回 末尾 元素值   [100, 2, '插入insert', 3, True, ['hello', 'word'], 129, 5]
print(popped)  # 5   [100, 2, '插入insert', 3, True, ['hello', 'word'], 129]

# 其他常用方法
print('获取列表长度：', len(my_list))  # 长度
print('记录列表中的值出现的次数：', my_list.count(2))  # 计数  [1, 2, 3,2, 'hello'] 列表中的 2  出现了2次
empy_list.sort()  # 排序 (同类型才行) 从小当大 降序
print('列表排序：', empy_list)
empy_list.reverse()  # 反转
print('列表反转：', empy_list)


"""
2. 元组（tuple）—— 不可变容器
   定义：用 () 或 tuple()。单元素要加逗号：(1,)
   特点：有序、不可变（定义后不能增删改）、允许重复。常用于固定数据或作为字典键。
"""
print()
my_tuple = (1, 2, 'hello', True, 2)
print('元组读取值：', my_tuple[0])
print('元组切片取值：', my_tuple[1:3])

# 元组是不可变的，改变会报错
# my_tuple[1] = 20
# my_tuple.append(2)

# tuple 常用：解包 (超级实用！)
a, b, c = (10, 20, 30)  # a=10 b=20 c=30
x, *rest = (1, 2, 3, 4)  # x=1 rest=[2,3,4]  (*收集剩余)

# 其他
print('tuple元组长度:', len(my_tuple))
print('tuple元组 元素出现的次数：', my_tuple.count(2))
print('tuple元组 返回第一次出现的次数：', my_tuple.index('hello'))  # 返回元素第一次出现的位置




print()
# 字典 dict
"""
3. 字典（dict）—— 键值对容器
定义：用 {} 或 dict()，格式 key: value。
特点：键唯一且不可变（常用 str、int、tuple），值任意；Python 3.7+ 保持插入顺序。
"""
my_dict = {'name':'anna','age':12,'city':'newyork'}
empty_dict = {}

#访问
print('字典访问值：',my_dict['name'])

#添加/修改
my_dict['age'] = 27  #修改
my_dict['score'] = 95 #新增  有匹配到的值就修改，没有匹配到的就新增
my_dict.update({'add':' new york 123445','sex':'男'}) #批量更新 有匹配到的值就修改，没有匹配到的就新增

#删除
del my_dict['age']  #删除
popped = my_dict.pop('add')  #删除 并返回值value
# print(my_dict)
my_dict.popitem() #删除回最后一对 （LIFO）并返回字典列表
# print('最后一对：',my_dict)

#常用方法
print('获取字典长度：',len(my_dict))
print('获取字典所有的key值：',type(my_dict.keys()),my_dict.keys()) #dict_keys(['name', 'city', 'score'])
print('获取字典所有的value值：',my_dict.values())  #dict_values(['anna', 'newyork', 95])
print('获取字典中所有的键值对：',type(my_dict.items()),my_dict.items())   #dict_items([('name', 'anna'), ('city', 'newyork'), ('score', 95)])

#遍历
for k,v in my_dict.items():
    print(f'{k}={v}')


#set集合
"""
4. 集合（set）—— 无序、不重复容器
定义：用 {} 或 set()（空集合必须用 set()）。
特点：无序、不允许重复、可变。常用于去重、成员测试、集合运算。
"""

my_set = {1,2,3,'hello',3} #重复的值会自动去掉 {1,2,3,'hello'}
empty_set = {}

#添加/删除
my_set.add(4) #添加
my_set.update([5,6]) #批量添加
my_set.remove(3)     #删除 (删除的元素不存在时会报错)
# print('set：',my_set)
my_set_pop = my_set.pop() #随机删除一个元素 并返回删除元素后的列表

#set集合运算
set1 = {1,2,3}
set2 = {3,4,5}
print('并集：',set1 | set2)  # 并集 {1,2,3,4,5} 将两个集合合并成一个，重复的去除
print('交集：',set1 & set2)  #交集 {3}  找出两个集合中都有的元素返回成一个新的集合set
print('差集：',set1 - set2)  #差集 {1,2}
print('对称差：',set1 ^ set2)       #对称差  {1,2,4,5}

#成员测试
print(2 in set1) #成员测试 true 2在set这个集合里面是否存在


# 容器之间相互转换
list_to_tuple = tuple([1,2,3,"helo",{'name':'anna'}])  #列表(list) 转 元组(tuple)
tuple_to_list = list((1,2,"hell"))  # 元组(tuple) 转 列表(list)
set_to_list = list({1,2,3,3}) # 集合(set) 转 列表(list) 去重
dict_keys_to_list = list(my_dict.keys())  # 字典(dict) 转  列表(list)

"""
嵌套容器（常见）
容器可以互相嵌套，比如列表里放字典、字典值是列表等（Pandas DataFrame 就类似嵌套容器）。
掌握这些，你就能轻松处理各种数据了！
"""