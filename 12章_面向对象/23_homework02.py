"""
练习题：2
1.文件中有 Grand、Father 和 Son，问：父类和子类中通过self和super()都可以调用哪些属性和方法
"""
class Grand:
    name = 'A'
    __age = 100
    def g1(self):
        #self 可以调用本类的，公开属性和私有属性
        print('Grand-g1()', self.name, self.__age)

class Father(Grand):
    id = '001'
    __score = None

    def f1(self):
        # super可以访问哪些成员: super().name  super().g1() ,只能访问父类的公开属性和公开方法，私有的属性和方法是访问不到的


        # self可以访问哪些成员: self.id,self.__score,self.name,self.g1() ，只能方法本类的的公开属性和公开方法和私有属性私有方法，父类的公开属性，公开方法
        # 继承的私有方法和私有属性都是不能访问的
        print(self.id,self.__score,self.name,self.g1())
        print('Father-n1()')

class Son(Father):
    name = 'B'

    def g1(self):
        print('Son-g1()')

    def __show(self):
        print('Son-show()')

# g = Grand()
# g.g1()
f = Father()
f.f1()
# s = Son()
# s.g1()

"""
一、第一句话（关于 super()）:
super() 可以访问父类及其祖先类中的公开属性和公开方法，
但不能‘直接’访问父类的私有属性和私有方法。
因为：
1.python私有属性：__age   其实会被改名 _Grand__age，所以super().__age访问不到
2.但理论上如果你知道真实的名字：super()._Grand__age 是可以访问的（但是不推荐）

二、第二句话（关于 self）
self 可以访问：
1. 本类的公开属性和公开方法
2. 本类的私有属性和私有方法
3. 父类和祖先类的公开属性和公开方法
但不能‘直接’访问父类的私有属性和私有方法。
"""
