"""
对目录的操作

# 案例
演示目录操作
    1) 创建一级目录 d://aaa
    2) 创建多级目录 d://bbb//ccc
    3) 删除目录 d://aaa 和 d://bbb//ccc
"""
import os
# 判断文件夹是否存在
# if os.path.isdir('/Users/apple/pandas_excel/aaa'):
#     print('aaa文件夹存在')
# else:
#     # 1.创建文件夹 创建一级目录
#     os.mkdir('/Users/apple/pandas_excel/aaa')

# 2.创建多集目录
# if os.path.isdir('/Users/apple/pandas_excel/bbb/ccc'):
#     print('/Users/apple/pandas_excel/bbb/ccc目录存在')
# else:
#     os.makedirs('/Users/apple/pandas_excel/bbb/ccc')

# 删除目录 /aaa  /bbb/ccc
# 删除单级目录使用rmdir,要求目录为空
# if os.path.isdir('/Users/apple/pandas_excel/aaa'):
#     os.rmdir('/Users/apple/pandas_excel/bbb')
# else:
#     print('目录不存在无法删除')


# 删除多集目录使用removedirs
# if os.path.isdir('/Users/apple/pandas_excel/bbb/ccc'):
#     os.removedirs('/Users/apple/pandas_excel/bbb/ccc')
# else:
#     print('文件夹不存在')