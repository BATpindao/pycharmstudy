# 数据容器练习
"""
题目 1：列表基本操作
创建一个列表 fruits = ["apple", "banana", "apple", "orange"]，然后：

去掉重复的 apple（只保留一个）。
在 "banana" 前插入 "grape"。
末尾添加 "kiwi"。
打印最终列表和长度。

思路：用 count/remove 或转为 set 再转回；insert、append、len。
"""

fruits = ['apple', 'banana', 'apple', 'orange']

# list 转 set 在转回 list
fruits_to_set = set(fruits) #无序去重
fruits = list(dict.fromkeys(fruits)) #有序去重
fruits = list(fruits_to_set)

# 在 列表 指定的位置 插入元素
fruits.insert(1, 'grape')
fruits.append('kiwi')
print('list:', len(fruits))

print()
"""
题目 2：元组解包
定义元组 person = ("Alice", 25, "Beijing", "Engineer")，用解包赋值给 name, age, city, job，然后打印 “我是{name}，{age}岁，来自{city}，职业{job}。”
思路：直接 a, b, c, d = person；或用 * 收集。
"""
person = ("Alice", 25, "Beijing", "Engineer")
name, age, city, job = person  # 自动解包 在函数里面要用func(*person)
print(f'我是{name},{age}岁，来自{city}，职业{job}')

print()
"""
题目 3：字典操作
创建一个字典 student = {"name": "Tom", "score": [85, 90, 78]}（成绩是列表）。

添加键 "age": 20。
修改第一门成绩为 95。
打印所有键和平均成绩。

思路：直接赋值新增；student["score"][0] 修改；sum()/len() 计算平均。
"""
student = {"name": "Tom", "score": [85, 90, 78]}

student['age'] = 20
student['score'][0] = 95
print(student.keys())
print('平均值：', sum(student['score']) / len(student['score']))

print()
"""
题目 4：集合去重与运算
有两个列表 list1 = [1, 2, 3, 4, 5]，list2 = [4, 5, 6, 7]。

转为集合，求并集、交集、只在 list1 中不在 list2 的元素。
打印结果。

思路：set(list1) | set(list2) 等运算。
"""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

list1_set = set(list1)
list2_set = set(list2)
print('并集：', list1_set | list2_set)
print('交集：', list1_set & list2_set)
print('差集：', list1_set - list2_set)

print()
"""
题目 5：嵌套字典
students = {
    "Alice": {"age": 25, "scores": [88, 92, 85]},
    "Bob": {"age": 22, "scores": [75, 80, 90]}
}

给 Alice 添加一门成绩 95。
计算 Bob 的平均成绩。
打印 Alice 的所有信息。

思路：students["Alice"]["scores"].append(95)；sum()/len()。
"""
students = {
    "Alice": {"age": 25, "scores": [88, 92, 85]},
    "Bob": {"age": 22, "scores": [75, 80, 90]}
}

students['Alice']['scores'].append(95)
average = sum(students['Bob']['scores']) / len(students['Bob']['scores'])
print('平均值：', average)

print('Alice-info:', students['Alice'])



print()
"""
题目 6：综合容器转换
有一个字符串 "hello world hello"。

转为列表，按空格 split。
用集合去重单词。

转为字典，键是单词，值是出现次数。
打印字典。

思路：str.split()；set() 去重；dict.fromkeys 或遍历计数。
"""
from collections import Counter
hello_str = 'hello world hello'
hello_list = hello_str.split(' ')
hello_set = set(hello_list)
print('单词计数字典',dict(Counter(hello_list)))
# 计数

