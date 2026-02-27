"""
1.字符串比较：
    .运算符：>,>=,<=,==,!=
    .比较规则：首先比较两个字符串的第一个1字符，如果相等则继续比较下一个字符，依次比较下去，
    直到两个字符串中的字符不相等时，起比较结果就是两个字符串的比较结果，两个字符串中的后续字符将不再比较
    .比较原理：两个字符进行比较时，比较的是其 ordinal value (原始值/码值) ，调用内置函数 ord 可以得到指定字符串的
    ordinal value 与内置函数 ord 对应的是内置函数 chr ，调用内置函数 chr 是指定 ordinal value 可以得到其对应的字符
"""

#  ord / chr 的使用
print(ord('a'))  # 97
print(chr(97))  # a

# 字符串比较
print('tim' <= 'tqm')

# 1.练习题
str_name = 'tom jack mary nono smith hsp lsp'
str_name_list =str_name.split(' ')

print(f'统计一共有：{len(str_name_list)}人名')

if str_name.count('hsp') >= 1:
    if str_name_list[str_name_list.index('hsp')].isalpha() == True:
        str_name_list[str_name_list.index('hsp')] = str_name_list[str_name_list.index('hsp')].capitalize()

print(str_name_list)

# 把列表中的首字母变为大写

for index in range(len(str_name_list)):
    str_name_list[index] = str_name_list[index].capitalize()

print('改变后的值：',str_name_list)


str_student = '123iphone mac imac air123'
print(str_student.strip("123"))


print('='*30)
# 切片
list_name = ['jack','Lisa','Paul','Smith','Smith','Kobe']
print('只去前三个名字：',list_name[0:3:1])
s = list_name[-1:-4:-1]
s.reverse() #reverse() 直接改变了列表原来的顺序 对元素进行逆序操作 反转操作
print('去后三个的名字保证原来的顺序：',s)