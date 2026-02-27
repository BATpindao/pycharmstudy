import numpy as np
import pandas as pd

# 使用列表、字典或数组创建一个默认索引的 Series。

# 使用list创建 Series
series_list = pd.Series([1, 2, 3, 4])
# 使用字典创建 Series
series_dict = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
# 使用 NumPy 数组创建 Series
series_numpy = pd.Series(np.array([1, 2, 3, 4]))

# 基本操作

# 指定索引创建series
s = pd.Series([1,2,3,4],index=['a','b','c','d'])

# 获取值
value = s['b'] #获取索引为 b 的值
key = s.iloc[2] #获取下标索引为2的值，s[2] 这种写法已经弃用 新写法 s.iloc[2]
print(value,key)

#获取多个值
print('获取多个值：\n',s[1:3])

print()
# 索引和值的对应关系
for index,value in s.items():
    print(f'{index}--{value}')

print()
# 使用切片语句来访问 series 的一部分
print(s['a':'c']) #返回索引 a 到 c 之间的索引 包括c
print(s.iloc[0:3])#切片索引，返回前三个元素

print()
# 为特定的索引标签赋值
s['a'] = 10 # 将索引标签 'a' 对应的元素修改为 10
# 通过赋值给新的索引标签赋值来添加新元素
s['e'] = 20 # 在 Series 中添加一个新的元素，索引标签为 'e'
# 使用del 删除指定索引的标签的元素
del s['a']  #删除一个没有的元素会报错
print(s)

print()
# 使用 drop 方法删除一个或多个索引标签，并返回一个新的 Series。
s_dropped = s.drop(['b','d'])  # 返回一个删除了索引标签 'b' 的新 Series
print(s_dropped)


#