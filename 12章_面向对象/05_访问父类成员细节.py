#1.子类不能直接访问父了的私有成员
# class A:
#     n1 = 100
#     __n2 = 200
#
#     def run(self):
#         print('A run()...')
#
#     def __jump(self):
#         print('A __jump()...')
#
# class B(A):
#     def say(self):
#         # 子类不能直接访问父类的私有成员
#         # print(A.__n2)
#         # print(super().__n2)
#         # A.__jump()
#         # super().__jump()
#         self.run()
#
# b = B()
# b.say()

# 2.访问不限于直接父类，而是建立从子类向上级类的查找关系 B->A->Base

class Base:
    n3 = 800
    def fly(self):
        print('base fly()...')

class A(Base):
    n1 = 100
    __n2 = 200

    def run(self):
        print('A run()...')

    def __jump(self):
        print('A __jump()...')

class B(A):
    def say(self):
        # 访问不限于直接父类，而是建立从子类向上级类的查找关系 A->B->Base...
        # Base.n3: 表示直接访问Base类的n3属性-》800
        # A.n3： 表示直接访问A类的n3 -> 800
        # super().n3: 表示从B类的直接父类A类去访问n3->800
        # self.n3: 表示从B类开始向上开始找 b-》a-〉base
        print(Base.n3,A.n3,super().n3,self.n3)

        # Base.fly(self): 表示直接访问Base的fly方法-> Base-fly()...
        # A.fly(self): 表示直接访问A类的fly方法-》Base-fly()...
        # super().fly(): 表示访问直接父类A的fly方法->Base-fly()...
        # self.fly() 表示访问本类B的fly方法->Base-fly()...
        Base.fly(self)
        A.fly(self)
        super().fly()
        self.fly()
        """
        细节：使用类名调用的方法和面要加self
                Base.fly(self)
                A.fly(self)
                super(),self    就不用加 self
        """

b = B()
b.say()

# 3.建议使用supper()的方式，因为如果使用父类名方式，一旦父类变化，类名统一需要修改，比较麻烦