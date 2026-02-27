"""
一、封装（Encapsulation）——“把细节藏起来”
python的封装是约定试的（靠命名约定），而不是强制式的 （不像Java/C#那么严格）
核心目的：
.隐藏内部实现细节
.保护数据不被随意修改
.提高代码可维护性

关键关键概念：
.私有属性和方法：通过将类的属性和方法设为私有的，来防止外部外部直接修改这些属性。python通过 _ 和 __前缀来区分公开和私有的成员：
    _ : 表示“受保护的”，通常不能直接访问，但可以被继承
    __ : 表示“私有的”，通常不能被外部访问，python会对其做“名称改写”以实现隐藏
"""

# python风格的封装层级（命名约定）
class Player:
    def __init__(self, name, hp):
        self.name = name  # 公开属性
        self._hp = hp  # 受保护 （约定：请不要直接修改）
        self.__mp = 100  # 私有的 （名字改写机制 Name Mangling）

    def get_mp(self):
        return self.__mp

    def set_mp(self, value):
        if 0 <= value <= 200:
            self.__mp = value
        else:
            print('mp值应在 0～200 之间')

    @property
    def mp(self): #推荐写法：用@property做“伪私有属性”
        return self.__mp

    @mp.setter
    def mp(self, value):
        if 0 <= value <= 200:
            self.__mp = value
        else:
            raise ValueError('mp值应在0～200之间')

    def attack(self):
        print(f"{self.name} 普通攻击！消耗了 10PM")
        self.__mp -= 10

"""
重要进阶知识：
1.私有属性其实能被访问：player._Player__mp（名字改写机制）
2.强烈推荐使用 @property + @xxx.setter / @xxx.deleter 来做属性封装
3.现代Python更倾向于用 dataclasses 或 pydantic 来做更优雅的封装
"""

# 使用 分装
p = Player('梅西','男')
print(p.name) #访问公开属性
print(p.get_mp()) #访问私有属性，通过公共方法
p.set_mp(120) #通过公共方法修改私有属性
print(p.get_mp())
