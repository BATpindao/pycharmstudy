"""
说明：编写工具函数，供程序员使用
"""

def read_confirm_select():
    """
    确认用户输入的是 y/n，不区分大小写，
    如果用户输入的不是 y/n 就反复输入
    :return:
    """
    is_ok = input('请输入你的选择(Y/N),请确认你的选择：').lower()
    while True:
        # 无论输入的是大写还是小写全部都转成小写

        if is_ok == 'y':
            return True
        elif is_ok == 'n':
            break
        else:
            is_ok = input('选择错误，请重新输入：').lower()




if __name__ == '__main__':
    print(read_confirm_select())