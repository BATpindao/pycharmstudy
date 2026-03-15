"""
1.拷贝文件：
    说明：将一张图片/一首歌 拷贝到另外一个目录下,要求使用read()和write()原生方法完成
"""
import os

# 创建一个文件夹
# if not os.path.exists('/Users/apple/pandas_excel/copy'):
#     os.mkdir('/Users/apple/pandas_excel/copy')
#
# if os.path.exists('/Users/apple/pandas_excel/jek.jpeg'):
#     print('文件存在')
#     with open('/Users/apple/pandas_excel/jek.jpeg','rb') as f_rb:
#         with open('/Users/apple/pandas_excel/copy/jek.jpeg','wb') as f_wb:
#             for line in f_rb:
#                 f_wb.write(line)

#删除文件
# os.remove('/Users/apple/pandas_excel/copy/jek.jpeg')
#删除文件夹
# os.rmdir('/Users/apple/pandas_excel/copy')

"""
2）实例递归遍历目录
# 遍历某个文件夹，判断它们分别是目录还是文件
"""
# file_path = '/Users/apple/pandas_excel'
# file_info_list = os.listdir(file_path)
# for file in file_path:
#     if os.path.isfile(file_path+'/'+file)
# print(file_info_list)