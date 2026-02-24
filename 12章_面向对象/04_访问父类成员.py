#调用父类成员细节
class A:
    n1 = 100

    def run(self):
        print('A-run()..')

class B(A):
    n1 = 200

    # say方法中通过 父类名 去访问父类的成员
    def say(self):
        print(f'父类的n1 {A.n1} 本类的n1 {self.n1}')
        # 调用父类的run
        A.run(self)
    #     调用本类的run
        self.run()


    # hi方法 通过super() 去访问父类的成员 super()相当于是一个 new对象 代表对象本身
    def hi(self):
        print(f'父类的n1 {super().n1}')
    #     调用父类的run()方法
        super().run()

    def run(self):
        print('B-run()..')


b = B()
b.say()
print('=='*20)
b.hi()