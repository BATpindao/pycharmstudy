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

2.文件打开模式：文本模式：r w，二进制模式: rb wb
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
读取文本文件时需要制定编码，读取的是字符编码，二进制文件不需要 读取的是二进制编码

1.文件常用的操作：
| 操作      | 函数          |
| ------- | ----------- |
| 创建/打开文件 | open()      | 如果文件不存在就会创建。
| 读取文件    | read()      | 读取文件全部的数据 read(size)size = 读取多少字符 read()不填就是读取整个文件
| 读取一行    | readline()  | 读取文件的一行数据
| 读取所有行   | readlines() | 读取文件的所有数据，并以list的形式返回
文件内容：
a
b
c
返回：['a\n','b\n','c\n']
| 写文件     | write()     | 将内容写入文件 write不会换行想要写入的内容换行的话就要加 \n
| 关闭文件    | close()     | 刷新并关闭此流，也就是f.flush()内置的flush功能
| 删除文件    | os.remove() | 如果文件不存在：会报错：FileNotFoundError import os  os.remove('文件名字')
| 推流(推送数据到磁盘文件)    | flus() | 将缓冲区数据 刷新写入文件
| 判断文件(文件夹)是否存在    | os.path.exists("test.txt") | 判断文件是否存在


open参数详解：
open(file文件路径, mode打开模式, encoding编码)
'w'、'a'、'x' 模式在文件不存在时会自动创建,其他的模式文件不存在时进行操作会报错文件不存error
mode常用的模式：
| mode | 含义    |
| ---- | ----- |
| r    | 读取    | 字符流用 (文本IO/文本文件)
| w    | 写入    | 字符流用 (文本IO)
| a    | 追加    |
| rb   | 读取二进制 | 字节流 (二进制IO/二进制文件)
| wb   | 写入二进制 | 字节流 (二进制IO)


推荐读取方式（最常用）：
with open("data.txt") as f:
    for line in f:
        # 一行一行的读取
        print(line.strip())
原因：节省内存，自动关闭文件

6 对目录的操作(文件夹)：
操作文件夹 要导包 import os
os.mkdir('文件夹路径') 创建文件夹(可以创建多级目录) 如果文件夹路径存在执行就会报错
os.makedirs('多级目录') 创建多级目录
os.rmdir('') 删除目录 注意：删除的目录必须为空，否则会删除失败
os.listdir('') 查看目录文件 返回目录下的所有文件(文件夹)名['.DS_Store', 'images', 'jek.jpeg', 'pandas_student.xlsx']
os.path是一个模块，它提供具体的函数来获取文件的信息

注意细节：
1.文件一定要关闭 close
2.大文件不要一次读取：
一次性读取会爆内存的
正确做法：
while True:
    # 一次性读取1024个字节，知道没有为止
    data = f.read(1024)
    if not data:
        break
3.文本文件要指定编码 不指定可能会出现 UnicodeDecodeError
"""
import os

# 判断文件是否存在 返回 true存在  false不存在
print('判断文件是否存在:',os.path.exists('/Users/apple/pandas_excel/jek.jpeg'))
# 判断是不是文件
print('判断是不是文件:',os.path.isfile('/Users/apple/pandas_excel'))
# 判断是不是目录
print('判断是不是目录:',os.path.isdir('/Users/apple/pandas_excel'))
# 获取文件大小 返回的是字节数 214213
print('获取文件大小：',os.path.getsize('/Users/apple/pandas_excel/jek.jpeg'))
# 获取文件的绝对路径
print('获取文件的绝对路径：',os.path.abspath('/Users/apple/pandas_excel/jek.jpeg'))






