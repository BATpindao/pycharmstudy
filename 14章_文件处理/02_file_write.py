"""
写文件：
需求:
1) 在d盘的a目录下创建  abc.txt 文件, 并写入10句 "hello, 韩顺平教育" 到文件
2) 将abc.txt 内容覆盖成新的内容10句 "hi, 老韩"
3) 在abc.txt 原有内容基础上追加10句 '你好! python'

细节：
1.mode = 'w' 打开文件，如果文件不存在，会创建，如果文件已存在，会截断打开的文件，也就是清空文件内容
2.如果我们希望以追加的方式写入，需要 mode='a'
"""
# f = open('/Users/apple/pandas_excel/hi.txt','w',encoding='utf-8')
f = open('/Users/apple/pandas_excel/hi.txt','a',encoding='utf-8')
# for i in range(10):
#     f.write("hello, 韩顺平教育\n")

# for i in range(10):
#     f.write("hi, 老韩\n")

for i in range(10):
    # 没有 \n 则表示没有换行  write写入成功返回的是写入的字符长度。写入失败返回 -1
    f.write("你好, python\n")

f.flush()
f.close()
