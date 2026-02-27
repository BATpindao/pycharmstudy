# string练习操作题

"""
题目 1：基本操作与切片
定义字符串 s = "Python is awesome!"

打印前5个字符。
打印倒数5个字符（用负索引）。
打印去除感叹号后的字符串。
打印整个字符串大写版本。

思路：切片 s[:5]、s[-5:]、replace 或切片去除、upper()。
"""

s = 'Python is awesome!'
print('打印前5个字符：', s[0:5])
print('打印去除感叹号的字符，', s[-5:])
print('打印去除感叹号后的字符串：',s[:-1])
print('字符串变大写：', s.upper())

print()
"""
题目 2：查找与替换
定义 s = "hello hello world"

统计 "hello" 出现次数。
.把第一个 "hello" 替换为 "hi"。
.查找 "world" 的位置。

思路：count()、replace()（只替换一次用正则或切片）、find() 或 index()。
"""
s = "hello hello world"

print('hello 出现次数:', s.count("hello"))  # 2

# 只替换第一个 hello
new_s = s.replace("hello", "hi", 1)  # 指定 count=1
print('只替换第一个:', new_s)              # 'hi hello world'

# 全替换（如果想全换）
# new_s = s.replace("hello", "hi")

print('world 位置:', s.find("world"))       # 12（find 更安全，找不到返回-1）
# 或 s.index("world")

print()
"""
题目 3：分割与连接
定义 s = "apple|banana|orange|kiwi"

用 "|" 分割成列表。
把列表中所有水果首字母大写，然后用 ", " 连接成新字符串。
打印结果。
"""

s = 'apple|banana|orange|kiwi'
new_list = s.split("|")
new_list = [i.title() for i in new_list]
print('列表转字符串:', ", ".join(new_list))

print()
"""
题目 4：判断与去除空白
定义 s = "  Python123  "
.去除两端空白后，判断是否全字母。
.判断是否以 "Py" 开头（不去空白）。
.判断是否全数字。
"""
s = "  Python123  "

stripped = s.strip()                        # 'Python123'
print('去除两端空白后是否全字母:', stripped.isalpha())  # False（有123）

print('是否以 "Py" 开头（不去空白）:', s.startswith("Py"))  # False（有空格）
print('是否全数字:', s.isdigit())          # False

print()
"""
题目 5：格式化综合
定义变量 name="Alice"、age=25、city="Beijing"、hobbies=["reading", "swimming"]

用 f-string 打印："我是Alice，今年25岁，来自Beijing，爱好：reading 和 swimming。"
用 .format() 实现同样输出。
"""
name = 'Alice'
age = 25
city = 'Beijing'
hobbies = ['reading', 'swimming']

print(f'我是{name}，今年{age}岁，来自{city}，爱好：{hobbies[0]}和{hobbies[1]}。')
print('我是{}，今年{}岁，来自{}，爱好：{}和{}。'.format(name, age, city, hobbies[0], hobbies[1]))

print()
"""
题目 6：复杂处理（稍难）
定义 s = "  Hello, World! Welcome to Python.  "

.去除所有空白（包括中间）。
.把所有单词首字母大写。
.把句子用 "-" 连接（无空格）。
.打印最终结果，如 "Hello-World-Welcome-To-Python"
"""
s = "  Hello, World! Welcome to Python.  "

# 方式1：彻底去除所有非字母（简单粗暴）
# s_clean = ''.join(c for c in s if c.isalpha() or c.isspace())  # 先保留字母和空格
# 更好方式：split() 默认处理多空格，然后去除标点

words = s.split()                           # ['Hello,', 'World!', 'Welcome', 'to', 'Python.']
# 去除标点（简单方式）
clean_words = [word.strip(".,!") for word in words]  # ['Hello', 'World', 'Welcome', 'to', 'Python']

capitalized = [word.title() for word in clean_words]
result = "-".join(capitalized)
print('最终结果:', result)                  # 'Hello-World-Welcome-To-Python'