# 循环 遍历 list
from operator import index

list_color = ['red','green','blue','yellow','white','black']

# while 1
print(len(list_color))
index = 0
while index < len(list_color):
      print(index+1,list_color[index] )
      index+= 1

print()
# for 1
for color in  list_color:
    print(color)

print ()
for index in range(len(list_color)):
    print(list_color[index])

"""
列表生成式
"""
print([i*i for i in range(1,11)])

"""
循环从键盘输入5个成绩，保存到列表，并输出
"""
# list_student = []
# for i in range(5):
#     scor = int(input('请输入成绩：'))
#     list_student.append(scor)
#     print(f'第{i+1},成绩：{scor}')
# print(list_student)
# print(f'这个班级的总成绩是：{sum(list_student)},平均分是：{sum(list_student)/len(list_student)}')

print()
print('求于数：',0//2)