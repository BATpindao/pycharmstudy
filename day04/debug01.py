# debug F8 逐行执行
from day01.demo_test1 import name_list

sum = 0
for i in range(11):
    sum += i
    print(f'i={i}')
    print(f'sum={sum}')

name_list = ['jorden', 'james', 'king', 'anna']
i = 0

while i<=len(name_list):
    print(name_list[i])
    i+=1
