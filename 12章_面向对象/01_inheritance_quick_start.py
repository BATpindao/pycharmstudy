#继承快速入门
class Student:
    __score = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 设置分数
    def set_score(self, score):
        self.__score = score

    # 展示学生信息
    def student_info(self):
        print(f'名字：{self.name}, 年龄：{self.age}, 分数：{self.__score}')

class Pupil(Student):
    def testing(self):
        print('...小学生正在考试。')

class Graduate(Student):
    def testing(self):
        print('...大学生正在考试生正在考试。')


p = Pupil('job',12)
p.set_score('90')
p.testing()
p.student_info()

print('='*20)

g = Graduate('anna',19)
g.set_score('80')
g.testing()
g.student_info()