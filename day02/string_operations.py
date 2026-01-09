# python 字符串(str) 操作 详解
"""
太好了！你已经掌握了数据容器，现在来学字符串（string）。
字符串是 Python 中最常用的数据类型之一，本质上是不可变（immutable）的字符序列（类似元组，但专为文本设计）。
字符串支持很多强大操作，常用于文本处理、数据清洗（Pandas 中也大量用到）。
"""

"""
1. 字符串基本特点
        .创建：用单引号 '、双引号 " 或三引号 '''（多行字符串）。
        .不可变：不能直接修改（如 s[0] = 'a' 会报错），修改必须创建新字符串。
        .支持索引、切片（像列表/元组）。
"""
s1 = 'hello world'  # 单引号
s2 = "hello world"  # 双引号
s3 = """多行
字符串"""  # 三引号 支持换行

# 字符串操作
print('字符串索引：',s1[0]) # h (索引从0开始)
print('字符串索引：',s2[-1]) # d (负索引末尾开始)
print('字符串切片：',s1[1:4]) #ell （切片，包前不包后）
print('字符串拼接:',s1+' '+s2) # hello world hello world 字符串链接
print('重复：',s3*3) #重复 打印

print()
"""
2. 常用字符串方法（超级实用！）
字符串有丰富内置方法（不改变原字符串，返回新字符串）。
"""
#大小写转换：
s = 'hello World!'
print('全部转大写：',s.upper()) #全部转大写
print('全部转小写：',s.lower()) #全部转小写
print('首字母大写：',s.title()) #首字母大写
print('句首大写：',s.capitalize()) #句首大写 Hello world!

#查找与替换
print('查找第一次出现的位置：',s.find('World')) # 6（返回首次位置，找不到返回-1）
print('返回元素出现的位置：',s.index('World')) # 6 返回元素首次出现的位置（找不到报错）
print('记录元素出现的次数：',s.count('l')) # 统计元素出现的次数
print('字符串替换：',s.replace('World','python')) #字符串替换。hello python!


print()
# 去除空白/分割/链接
s = '  hello  '
print('去除字符串两边的空格:',s.strip()) #去除字符串两端空格
print('去除字符串左边的空格:',s.lstrip()) #去左空格
print('去除字符串右边的空格:',s.rstrip()) #去右空格

s = 'apple,huawei,oppo'
print('字符串拆分成列表：',s.split(","))

fruits = ['apple', 'banana', 'orange']
print(','.join(fruits)) #列表转字符串 apple,banana,orange


print()
# 判断方法（返回True/False）
print('123'.isdigit()) #判断是不是全是数字
print('qwe'.isalpha()) #判断是不是全是字母
print('123qwe'.isalnum()) #判断字母或数字 123qwe=True  123=true  qwe=true 只=true ---=false
print('hello'.startswith('he')) #判断 字符串是不是以 he 开头
print('hello'.endswith('lo'))  #判断 字符串是不是以 lo 结尾

print()
print('hello'.center(20,'-')) #剧中填充  ——width:总共填充的宽度 ，————fillchar:填充的内容


print()
# 3. 字符串格式化
"""
把变量插入字符串的几种方式：
"""
name = 'Tom'
age = 23

# f-string
print(f'我是：{name},年龄：{age}')
print(f'明年：{age+1}') # f-string 支持表达式

#.format()
print('我是：{},今年：{}'.format(name,age))
print('我是：{name},今年：{age}'.format(name='jek',age=12))

# % 格式化 不推荐 %s 表示字符串  %d 表示数字 int
print('我是%s,今年%d'%(name,age))

print()
# 4. 转义字符
# \n：换行
# \t：制表符
# \\：反斜杠
# \' 或 \"：引号

print("hello\nworld")  # 换行输出
print(r"C:\new\test")  # r 前缀：原始字符串（不转义）


print()
#5.字符串与容器
print('字符串转列表',list('hello'))
print('列表转字符串：','.'.join(['mac','mini','m4']))