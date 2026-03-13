"""
1.拷贝文件：
    说明：将一张图片/一首歌 拷贝到另外一个目录下,要求使用read()和write()原生方法完成
"""
# 方式1: 使用read()和write()方法
# f_image_r = None
# f_image_w = None
# try:
#     f_image_r = open('/Users/apple/pandas_excel/jek.jpeg', 'rb')
#     f_image_w = open('/Users/apple/pandas_excel/like_jek.jpeg', 'wb')
#
#     image = f_image_r.read()
#     f_image_w.write(image)
#
# except Exception as e:
#     print(e)
#
# finally:
#     if f_image_r:
#         f_image_r.close()
#     if f_image_w:
#         f_image_w.close()


# 方式二：with open() 我们再使用with子句的方式完成文件拷贝(读取一行数据, 就写入)
with open('/Users/apple/pandas_excel/jek.jpeg','rb') as f_r:
    with open('/Users/apple/pandas_excel/like_jek.jpeg','wb') as f_w:
        for line in f_r:
            f_w.write(line)
