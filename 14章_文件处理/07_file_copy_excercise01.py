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

# 删除文件
# os.remove('/Users/apple/pandas_excel/copy/jek.jpeg')
# 删除文件夹
# os.rmdir('/Users/apple/pandas_excel/copy')

"""
2）实例递归遍历目录
# 遍历某个文件夹，判断它们分别是目录还是文件
"""

"""
1.判断是文件还是目录

"""
def traversal_file(file_path: str):
    if os.path.isdir(file_path):
        print(f'是目录--',file_path)
        file_list = os.listdir(file_path)
        for f in file_list:
            if os.path.isfile(os.path.join(file_path,f)):
                print(f'是文件--',os.path.join(file_path,f))
            else:
                traversal_file(os.path.join(file_path,f))
    else:
        print(f'是文件--',file_path)


if __name__ == '__main__':
    traversal_file('/Users/apple/pandas_excel')

"""
进阶版
import os

def traversal_file(file_path: str, level=0):
    indent = '  ' * level

    if os.path.isdir(file_path):
        print(f'{indent}📁 目录-- {file_path}')
        try:
            for entry in os.listdir(file_path):
                full_path = os.path.join(file_path, entry)
                traversal_file(full_path, level + 1)
        except Exception as e:
            print(f'{indent}⚠️ 无法访问: {file_path}, 原因: {e}')
    else:
        print(f'{indent}📄 文件-- {file_path}')


if __name__ == '__main__':
    traversal_file('/Users/apple/pandas_excel')
"""

