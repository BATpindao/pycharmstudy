"""
DataFrom 构造方法
    pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
    参数说明：
    data：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
    index：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
    columns：DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
    dtype：指定 DataFrame 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
    copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
"""
import pandas as pd
import numpy as np

# 用列表创建DataFrom
data = [['google',12],['x',21],['apple',14]]
# 创建DataFrom
df = pd.DataFrame(data, columns=['name','age'])

# 用atype方法设置，每列的数据类型
df['name'] = df['name'].astype('str')
df['age'] = df['age'].astype('float')
print(df)
"""
     name   age
0  google  12.0
1       x  21.0
2   apple  14.0
"""


print()
# 使用字典创建 DataFrom  创建时 DataFrom 时data这里的数量要对应起来一样多
student_data = {'name':['anna','tom','jec','luc'],'sex':[12,23,53,32]}
student_df = pd.DataFrame(student_data)
print(student_df)
"""
   name  sex
0  anna   12
1   tom   23
2   jec   53
3   luc   32
"""

print()
# 使用ndarray
ndarry_data = np.array([
    ['google',10],
    ['x',20],
    ['apple',30],
])
# 使用DataFrom构造函数创建数据帧
ndarry = pd.DataFrame(ndarry_data,columns=['name','age'])
# 打印数据帧
print(ndarry)
"""
     name age
0  google  10
1       x  20
2   apple  30
"""

print()
# 使用 列表-字典data  没有对应的部分数据为NaN
list_dict_data = [{'a':1,'b':2},{'a':5,'b':10,'c':91}]
ldd = pd.DataFrame(list_dict_data)
print(ldd)
"""
   a   b     c
0  1   2   NaN
1  5  10  91.0
"""

print()
# pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为0，第二行为1，以此类推
"""
   name  sex
0  anna   12
1   tom   23
2   jec   53
3   luc   32
"""
# 返回第一行
print(student_df.loc[0])
# 返回第二行
print(student_df.loc[1])