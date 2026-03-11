"""
工具类
1.编写utility类【工具类】
2.提供各种方法
"""
class Utility:
    @staticmethod
    def read_confirm_select()->bool:
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
                return False
            else:
                is_ok = input('选择错误，请重新输入：').lower()
