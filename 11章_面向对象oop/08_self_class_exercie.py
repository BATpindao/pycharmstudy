# 定义Person类
# 1) 里面有name、age属性
# 2) 并提供compare_to比较方法，用于判断是否和另一个人相等
# 3) 名字和年龄都一样，就返回True, 否则返回False

class Person:
    name = None
    age = None

    def compare_to(self,person):
        if self.name == person.name and self.age == person.age:
            return True
        else:
            return False

p1 = Person()
p1.name = 'tom'
p1.age = 20

p2 = Person()
p2.name = 'tom'
p2.age = 20

# 开始比较

i = p2.compare_to(p1)
print(i)