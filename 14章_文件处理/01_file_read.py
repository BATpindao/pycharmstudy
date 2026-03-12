"""
1.创建文件：
我们创建一个文件，只需要以model = ‘w’ 形式打开文件即可
如果文件hi.txt不存在，系统会创建该文件,如果文件存在则创建一个新的文件覆盖掉旧的文件，新的的文件什么数据也没有
注意 encoding是一个关键字参数，encoding不是open()方法的第三个参数
"""
# f = open('/Users/apple/pandas_excel/hi.txt','w',encoding='utf-8')
# print(type(f)) #<class '_io.TextIOWrapper'>

"""
2.读取文件：
需求：读取在/Users/apple/pandas_excel 下的text.txt文件
"""

f = open('/Users/apple/pandas_excel/text.txt','r',encoding='utf-8')
# read 一次返回整个文件的内容
# print(f.read())
# read(2)读取文件的两个字符
# print(f.read(2))


print('text.txt'.center(31,'='))

# 读取方式2 readlines 注意readlines读取文件一行的数据，字符串结尾会保留 \n换行
# print(f.readline().rstrip('\n'))
# print(f.readline().rstrip('\n'))
"""
输出的结果：
你好 世界🪢

jec
如果不想要这个 \n的话 就用rstrip('\n')把它截取掉
"""

# 读取方式3 with open()
#             for line in f:
# with open('/Users/apple/pandas_excel/text.txt','r',encoding='utf-8') as f:
#     for line in f:
#         # 默认有换行
#         print(line,end='')


# 4. f.readlines 一列表的形式读取文件
# print(f.readlines()) #['你好 世界🪢\n', 'jec\n', 'you ni hao']


# 读取方式5: for line in f形式读取文件
for line in f:
    print(line,end='')
"""
去除了 \n
你好 世界🪢
jec
you ni hao
"""

# close关闭文件，释放文件占用的系统资源
f.close()