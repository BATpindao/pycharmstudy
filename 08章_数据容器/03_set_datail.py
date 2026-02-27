"""
set的定义：
    {}
    set是一个 无序，不可重复的集合
无序，也就是你定义元素的顺序和取出的顺序不能保证一致，
集合底层会按照自己的一套算法来存储和取出数据，所以每次取出顺序是不变的

set里面有重复项的话会自动去重
"""
set_a = {100, 200, 300, 400, 500, 600}

print(set_a)

# set不支持索引
# print(set_a[0]) # 'set' object is not subscriptable

# set 循环 只能用for 不能用while应为不能用下标

for item in set_a:
    print(item)

# 创建一个空的set 要用 set() ,不能用 {} 这样会创建一个空字典
set_b = {}
set_c = set()

print(type(set_b), type(set_c))  # <class 'dict'> <class 'set'>

# set集合的一些常用方法

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}

# len() 集合中元素的个数
print('basket元素的个数', len(basket))

# in 判断元素在集合中是否存在
print('mac' in basket)

# pop 删除集合中的任意一个元素,并返回删除的元素值  ，这个操作会影响愿集合
print(basket.pop())

#  clear 删除列表中的所有元素 ， 操作会影响原列表
basket.clear()
print(basket)

# 练习题
s_history = {"小明", "张三", "李四", "王五", "Lily", "Bob"}
s_politic = {"小明", "小花", "小红", "二狗"}
s_english = {"小明", "Lily", "Bob", "Davil", "李四"}

print("====" * 15)
# 求选课学生共有多少人 并集
student_len = s_english | s_politic | s_history
print('选课人有：', len(student_len))

# 求只选了第一个学科（history）的学生数量和学生姓名 （差集）
student_cha = s_history - s_politic - s_english
print(f'history的学生数量：{len(student_cha)},名字是：{student_cha}')

# 求只选了一门学科的学生数量和学生姓名  差集 -  并集 ｜
student_1 = s_history - s_politic - s_english
student_2 = s_politic - s_history - s_english
student_3 = s_english - s_history - s_politic

# print(f'只选了一门课的学生：{len(student_1)+len(student_2)+len(student_3)} 和学生名字：{student_1 |student_2 | student_3}')
print(f'只选了一门课的学生：{len(student_1 | student_2 | student_3)} 和学生名字：{student_1 | student_2 | student_3}')

# 求选了三门学科的学生数量和学生姓名 交集

student_jiao = s_history & s_politic & s_english
print(f'选了三门课的学生数量：{len(student_jiao)}，名字是：{student_jiao}')

print()

