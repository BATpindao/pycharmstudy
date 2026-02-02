def hi():
    print('hsp hi!')

def ok():
    print('hsp ok!')

# 在main中写测试代码，其他模块引入该文件时则不会执行该测试代码
if __name__ == '__main__':
    hi()
print('hsp_hi--name--', __name__)
