"""
1.什么是文件操作
    文件操作就是 程序对磁盘文件进行读写
例如：
    。读取配置文件
    。保存用户数据
    。写日志
    。导出数据
python提供得核心函数是：
    open()
f = open(文件路径，打开模式，编码)
例如：
f = open("test.txt", "r", encoding="utf-8")

2.文件打开模式
| 模式 | 含义         |
| -- | ---------- |
| r  | 只读（文件必须存在） |
| w  | 写入（会清空原文件） |
| a  | 追加写入       |
| rb | 读二进制       |
| wb | 写二进制       |

例如：
f = open("data.txt", "w", encoding="utf-8")
打开 data.txt 文件
写入模式
格式是：utf-8编码
如果文件不存在会自动创建

3.读取文件
读取文件有三种常见的方式：

read() 读取全部
"""
# f = open('/Users/apple/pandas_excel/text.txt','r',encoding="utf-8")
# f.read()读取全部
# content = f.read()
# print(content)

# readline() 读取一行
# print(f.readline())

#readlines() 读取所有行 返回一个list列表,每个元素就是一行的数据
# content = f.readlines()
# print(content)

# 释放资源
# f.close()

"""
遍历文件最常用的 for循环读取
优点：
    .节省内存
    .适合大文件
"""
# f = open('/Users/apple/pandas_excel/text.txt','r',encoding="utf-8")
# for line in f:
#     # rstrip 去除尾端后面的字符
#     print(line.rstrip('\n'))
# f.close()

"""
5.写入文件
write
w模式会 清空 文件的旧数据
"""
# file_w = open('/Users/apple/pandas_excel/text.txt','w',encoding="utf-8")
# file_w.write('你好 世界🪢\n')
# file_w.write('jec\n')
# file_w.close()

"""
6.追加写入：
    如果不想覆盖原文件，只是追加数据，用a模式
"""
# file_write = open('/Users/apple/pandas_excel/text.txt','a',encoding='utf-8')
# file_write.write('you ni hao')
# file_write.close()

"""
7.关闭文件 （关闭）
f.close()
如果不关闭：
    。可能导致数据未写入
    。文件被占用
"""

"""
8.推荐写法 （with）
python最推荐的方式：

优点：
    。自动关闭文件
    。更安全
    
等价于：
f = open(...)
try:
    ...
finally:
    f.close()
"""
with open('/Users/apple/pandas_excel/text.txt','r',encoding='utf-8') as f:
    print(f.read())

