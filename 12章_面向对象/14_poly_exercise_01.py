# python 练习题 1

class A:
    i = 10

    # 当调用对象成员的时候，会和对象本生动态关联
    def sum(self):
        return self.get1() + 10

    def sum1(self):
        return self.i + 10

    def get1(self):
        return self.i

class B(A):
    i = 20

    # def sum(self):
    #     return self.get1() + 20

    def sum1(self):
        return self.i + 10

    def get1(self):
        return self.i

#   创建B 对象
b = B()
print(b.sum()) # 40 30
print(b.sum1()) #30