"""
flush(): 刷新流的写入缓冲区到文件
1.调用 f.wirte(),内容并没有真正写入到文件，而是先积攒到缓存区
2.当调用flus()时，内容会真正写入到文件
3.这样是为了避免的操作硬盘，导致效率低，(积攒一定量的数据，一次性写入文件，提高效率)
"""
import time

# f = open('/Users/apple/pandas_excel/text.txt','a',encoding='utf-8')
# f.write('你好1， python\n')
# f.write('你好2， python\n')
# f.write('你好3， python\n')
#
# print('等待'.center(40,'='))
# time.sleep(10) #sleep是以秒为单位的  休眠时间
# print('结束'.center(40,'='))


# 测试 f.flush()将缓冲区数据 刷新写入文件
# f.flush()

"""
2.f.close(): 刷新并关闭此流，也就是f.flush()内置的flush功能
3.with open() as f:在处理文件对象时，字句体结束后，文件会自动关闭
"""

# 在处理文件对象时，字句体结束后，文件会自动关闭
with open('/Users/apple/pandas_excel/text.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print('-------文件内容---------')
    for line in lines:
        print(line,end='')
# closed 检测文件对象是否关闭，true文件已关闭 false文件未关闭
print(f'\n文件是否关闭 ->:{f.closed}')


