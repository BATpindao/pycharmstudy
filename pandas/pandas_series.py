"""
Pandas 数据结构 - Series
Series 是 Pandas 中的一个核心数据结构，类似于一个一维的数组，具有数据和索引。
Series 可以存储任何数据类型（整数、浮点数、字符串等），并通过标签（索引）来访问元素。
Series 的数据结构是非常有用的，因为它可以处理各种数据类型，同时保持了高效的数据操作能力，比如可以通过标签来快速访问和操作数据。

Series 特点：
一维数组：Series 中的每个元素都有一个对应的索引值。
索引： 每个数据元素都可以通过标签（索引）来访问，默认情况下索引是从 0 开始的整数，但你也可以自定义索引。
数据类型： Series 可以容纳不同数据类型的元素，包括整数、浮点数、字符串、Python 对象等。
大小不变性：Series 的大小在创建后是不变的，但可以通过某些操作（如 append 或 delete）来改变。
操作：Series 支持各种操作，如数学运算、统计分析、字符串处理等。
缺失数据：Series 可以包含缺失数据，Pandas 使用NaN（Not a Number）来表示缺失或无值。
自动对齐：当对多个 Series 进行运算时，Pandas 会自动根据索引对齐数据，这使得数据处理更加高效。

pd.Series(data=None, index=None, dtype=None, name=None, copy=False)
data: Series 中存放的数据本体  ⚠️：如果是 dict，key 会自动成为 index
index: 指定series的索引标签  不指定：自动生成默认 (0,1,2....)   指定了：长度必须和data一样长 (dict列外)
dtype:指定data的数据类型
name: 给series起一个名字
copy:作用：是否复制数据（避免和原始数据共享内存）
"""
import pandas as pd

"""
创建一个series对象，指定列名A 直是 1，2，3，4
默认索引是 0，1，2，3
"""
series = pd.Series([1,2,3,4],name='A')
print(series) #显示series对象

# 显示的设置索引
custom_index = [1,2,3,4] #自定义索引
custom_series = pd.Series([1,2,3,4],name='A',index=custom_index)
#显示带自定义的索引series
print(custom_series)

print()
a = [1, 2, 3] #用列表来创建series
myvar = pd.Series(a)
print(myvar)
print('series(索引)取值：',myvar[0])
"""
输出
索引 数据
0    1
1    2
2    3
dtype: int64 数据类型
"""

print()
# 指定索引值，取值的使用

name = ['iphone','google','huawei']
name_index = ['i','g','h']
series_st = pd.Series(name,index=name_index)
print(series_st)
print('自定义索引取值：',series_st['g'])


print()
# 用dict字典来当作数据 key:value
series_dict = {1:'google',2:'iphone',3:'huawei'}
sites = pd.Series(series_dict)
print(sites)
"""
输出：
1    google
2    iphone
3    huawei
dtype: object
从输出可以看出：key的值变成了索引
如果我们只需要字典中的一部分数据，只需要指定需要的数据的索引即可
"""
# 指定需要的数据索引，设置series参数的名字
my_dict_series = pd.Series(series_dict,index=[2,3],name='gs_name')
print(my_dict_series)
"""
输出：
2    iphone
3    huawei
Name: gs_name, dtype: object
"""

