import pandas as pd  # 标准别名 pd
import numpy as np  # pandas 常配合 NumPy 用 （可选）

"""
2. Series：一维数据结构（像带索引的列表）
    .Series 是 Pandas 的基本构建块，类似带标签的数组。
"""

# series创建
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])  # 自定义索引
print('自定义索引：', s1)
"""
输出：
a    1
b    2
c    3
d    4
dtype: int64
"""

# 从字典创建 （键变索引）
s2 = pd.Series({'name': 'Alic', 'age': 25, 'city': 'Beijing'})
print('从字典创建：:', s2)
"""
name       Alic
age          25
city    Beijing
dtype: object
"""

# 默认索引 （0开始）
s3 = pd.Series([10, 20, 30])
print(s3[1])  # 20 (位置索引)
# print(s3['1']) #错误！默认索引是整数 用标签自定义
"""
20
"""

print()
# 基本操作
print('获取 series 的值：', s1.values)  # array([1, 2, 3, 4])（底层 NumPy 数组）
print('获取 series 的索引：', s1.index)  # Index(['a', 'b', 'c', 'd'])
print('获取 series 的平均值：', s1.mean())  # 平均值 2.5
print('统计摘要：', s1.describe())  # 统计摘要

print()
"""
3. DataFrame：二维表格结构（Pandas 核心，像 Excel 表）
       .DataFrame 是最常用的，行+列+索引。
       .创建方式：
"""
# 从字典创建 (键变列名)
data = {
    'name': ['Alice', 'Bob', 'Tom'],
    'age': [25, 30, 22],
    'city': ['Beijing', 'Beijing', 'shanghai']
}

df = pd.DataFrame(data)
print(df)
"""
输出：
    name  age     city
0  Alice   25  Beijing
1    Bob   30  Beijing
2  Tom     22  Beijing
"""

print()
# 从列表创建 （需指定 columns）
df2 = pd.DataFrame(
    [
        ['Alice', 25, 'beijing'],
        ['bob', 30, 'shanghai']
    ], columns=['name', 'age', 'city'], index=['A', 'B']
)  # 自定义索引

print(df2)

print()
# 数据查看神器
print(df.head(2))  # 前2行  获取前两行的数据
print(df.tail(1))  # 后一行 获取最后 ‘几’ 行的数据
print(df.sample(2))  # 随机2行 随机获取两行数据
print('获取结构信息')
print(df.info())  # 结构信息 （列类型 ，非空数）
print(df.describe())  # 数列统计（mean,std 等）
print(df.shape)  # (3,3) 行数 ， 列数
print(df.dtypes)  # 每列的类型
print(df.columns)  # 列名
print(df.index)  # 行索引

# 读写文件
# 读 csv（下载一个 Titanic.csv 测试）
# df_csv = pd.read_csv("titanic.csv")  # 参数：sep=','、encoding='utf-8' 等

# 读 Excel
df_excel = pd.read_excel("/Users/apple/pandas_excel/pandas_student.xlsx", sheet_name="Sheet1")
print('excel数据：', df_excel.columns)

# 写文件
# df.to_csv("output.csv", index=False)  # 不写行索引
# df.to_excel("/Users/apple/pandas_excel/output.xlsx", index=False)


print()
# 4.基本索引与切片 (重点)
#  .列选择：
print(df['name'])  # series 单列
print(df[['name', 'age']])  # datadrame 多列

# 添加和删除列
df['score'] = [85, 90, 78]  # 添加新列
del df['score']  # 删除
# df.drop('age',axis=1,inplace=True)  # 安全删除 （axis = 1 列）
print(df)

print()
"""
行选择 (核心区别)
"""
# 位置索引：iloc （整数位置）
print(df.iloc[0])  # 获取第一行的数据
print(df.iloc[0:2])  # 获取前两行 dataframe
print(df.iloc[0, 1])  # 第1行第2列值（age）

# 标签索引 ： loc (行/列标签)
print(df.loc[0])  # 第0行 (默认整数索引)
print(df.loc[0:1, 'name':'age'])  # 行 0-1，列name 到age（包含末尾！）
print(df.at[0, 'name'])  # 单值快速访问

print()
# 布尔索引 (过滤神器)
print(df[df['age'] > 25])  # 年龄>25的行
print(df[(df["age"] > 20) & (df["city"] == "Beijing")])  # 多条件
