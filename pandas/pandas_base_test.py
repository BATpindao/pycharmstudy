import pandas as pd
import numpy as np

"""
题目 1：创建 Series 和基本操作
创建 Series：成绩 = pd.Series([85, 90, 78, 92], index=["数学", "英语", "语文", "物理"])

打印平均分。
打印最高分和科目。
打印所有大于85的分数。
"""
score = pd.Series([85, 90, 78, 92], index=['数学', '英文', '语文', '物理'])

print(score)

print('平均值:', score.mean())
print(f'最高分:{score.max()} ,科目:{score.idxmax()}')
print('所有分数大于85的分数：')
print(score[score > 85])

print()
"""
题目 2：创建 DataFrame
用字典创建学生表：
data = {"name": ["Alice", "Bob", "Tom"], "age": [25, 30, 22], "score": [85, 90, 78]}

打印 info() 和 describe()。
添加列 "gender": ["F", "M", "M"]。
打印前2行。

思路：pd.DataFrame()、info()/describe()、新列赋值、head()。
"""
data = {
    'name': ['Alice', 'Bob', 'Tom'],
    'age': [25, 30, 22],
    'score': [85, 90, 78]
}
student_score_info = pd.DataFrame(data)
print('打印info()信息：')
print(student_score_info.info())

print()
print('打印 describe():')
print(student_score_info.describe())

print('添加列：')
student_score_info['gender'] = ['F', 'M', 'M']
print(student_score_info)

print('打印前两行：')
print(student_score_info.iloc[0:2])

print()
"""
题目 3：读文件（需准备文件）
下载 Titanic.csv（Kaggle 免费），用 pd.read_csv 读入 df。

打印 shape、columns、head(5)。
打印 "Survived" 列的 value_counts()。

思路：read_csv()、基本查看方法。
"""

student = pd.read_excel("/Users/apple/pandas_excel/pandas_student.xlsx",sheet_name="Sheet1")
print(student)

print('打印excel文件中占用的 行数 列数 ：',student.shape) #打印 行数 列数
print('打印excel文件中所有的列名：',student.columns) #打印列名
print('获取excel文件中前一行的数据：')
print(student.head(1))

print()
print(student.value_counts())
