"""
6.获取文件的相关信息

st_size: 文件大小（以字节为单位），
"""
import os
import time

f_stat = os.stat('/Users/apple/pandas_excel/hi.txt')
print('--------文件信息----------')
print(f'文件大小-> {f_stat.st_size}')
print(f'最近的访问时间-> {time.ctime(f_stat.st_atime)}')
print(f'最近的修改时间-> {time.ctime(f_stat.st_mtime)}')
print(f'文件创建时间-> {time.ctime(f_stat.st_ctime)}')