"""
python中实现多个构造函数
https://www.cnblogs.com/kingwz/p/16335499.html
"""
class Rect:
    __length = 0
    __width = 0

    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    @classmethod
    def initsec(self, l):
        # 记得返回self
        return self(l, l)

    def e(self):
        return self.__width * self.__length


# 使用方法和init不同
t = Rect.initsec(1)
print(t.e())
t = Rect(2, 4)
print(t.e())
