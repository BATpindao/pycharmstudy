"""
练习题：3
1.编写Doctor类，属性：name， age， job， gender， sal 5个参数的构造器，重写__eq__()方法，
2.并判断测试类中创建的两个对象是否相等（相等就是判断属性是否相同）。
"""
class Doctor:
    def __init__(self, name, age, job, gender):
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age and self.job == other.job and self.gender == other.gender:
            return True
        else:
            return False

d1 = Doctor('job',12,'java','男')
d2 = Doctor('tom',14,'java','男')

print(d1.__eq__(d2))
