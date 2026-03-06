"""
练习题1
1.定义一个Person类，属性：name，age，job，创建Person，有3个person对象，并按照age从大到小排序。
"""

class Person:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job

    # 重写输出方法
    def __str__(self):
        return f'{self.name},{self.age},{self.job}'

p1 = Person('jek',21,'python')
p2 = Person('tom',31,'java')
p3 = Person('luc',27,'c++')
p4= Person('jec',40,'ruby')

# 排序方法1 使用sort
person_list = [p1,p2,p3,p4]
# person_list.sort(key=lambda p:p.age,reverse=True)
# for person in person_list:
#     print(person)

# 方式二 冒泡排序  从大到小排序
def bubble_sort(person:list[Person]) -> list[Person]:
    n = len(person)
    new_arr = person[:]
    for i in range(n):
        for j in range(n):
            if new_arr[j].age<new_arr[i].age:
                new_arr[j],new_arr[i] = new_arr[i],new_arr[j]

    return new_arr

person_sort = bubble_sort(person_list)
for person in person_sort:
    print(person)