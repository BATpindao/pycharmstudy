"""
9.实战案例：
案例1：读取日志
log.txt
"""
# with open('/Users/apple/pandas_excel/login.txt','r',encoding='utf-8') as f:
#     for line in f:
#         # 去除空格
#         print(f'日志：{line.rstrip('\n')}')
"""
日志：error
日志：warning
日志：info
"""

"""
案例2：保存用户数据
"""
# name = input('请输入姓名：')
# age = input('请输入年龄：')
# with open('/Users/apple/pandas_excel/login.txt','a',encoding='utf-8') as f:
#     # 后面要加 \t 才可以写入的数据才会换行
#     f.write(name+','+age+'\t')

"""
案例3：统计文件行数

count = 0

with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        count += 1

print("行数:", count)
"""
# count = 0
# with open('/Users/apple/pandas_excel/text.txt','r',encoding='utf-8') as f:
#     count = len(f.readlines())
# print('文件行数：',count)


"""
10.文件指针（简单了解）
文件读取有个 指针位置 f.read()

读取后指针到文件末尾。

再次读取 f.read() 结果‘’ 应为读取完了

可以用f.seek(0)回到开头就又可以读取到内容了
"""
f =open('/Users/apple/pandas_excel/text.txt','r',encoding='utf-8')
# print(f.read())
# f.seek(0)
# print(f.read())
# f.close()
# 以列表的形式，读取文件中所有的行
print(list(f))
"""
文件操作的五个重点：
open() 打开文件
read() 读取文件内容
write() 写入内容到文件
with open()  with简化文件读写操作
for line in f
"""