"""
删除文件：

"""
# 引入os模块,它提供了一些文件的操作
import os

if os.path.exists('/Users/apple/pandas_excel/hello.txt'):#判断文件是否存在
    # 没有返回值
    os.remove('/Users/apple/pandas_excel/hello.txt')#删除文件
else:
    print('文件不存在')

