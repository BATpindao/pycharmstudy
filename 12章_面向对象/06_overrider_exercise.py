"""
面向对象 - 重写
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f'名字：{self.name}，年龄：{self.age}'


class Student(Person):
    def __init__(self, name, age, id, score):
        super().__init__(name, age)
        # 新增的属性
        self.id = id
        self.score = score

    def say(self):
        return f'id:{self.id},{super().say()},分数：{self.score}'


s = Student('king', 15, '001', 98)
print(s.say())
