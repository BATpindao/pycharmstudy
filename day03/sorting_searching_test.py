"""
1.内置排序基础
给定一个无序列表 [64, 34, 25, 12, 22, 11, 90]，分别用 sorted() 和 list.sort() 实现升序和降序排序，并打印结果。
"""
sort_list = [64, 34, 25, 12, 22, 11, 90]

sorted_list_asc = sorted(sort_list)
print('sorted 升序：', sorted_list_asc)
sorted_list_desc = sorted(sort_list, reverse=True)
print('sorted 降序：', sorted_list_desc)

print()

sort_list.sort(reverse=False)
print('sort 升序', sort_list)
sort_list.sort(reverse=True)
print('sort 降序', sort_list)

print()
"""
2.自定义排序
有列表 students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]，按成绩从高到低排序（成绩是第二个元素）。
"""
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1], reverse=True)
print('降序：', students)

print()
"""
3.手写冒泡排序
实现冒泡排序函数 bubble_sort(arr)，返回排序后的新列表（不要修改原列表）。测试数据：[5, 3, 8, 4, 2]。
"""


def bubble_sort(arr):
    n = len(arr)
    new_arr = arr[:]  # 重新创建一份新的
    for i in range(n):
        for j in range(n - i - 1):
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr


nums = [5, 3, 8, 4, 2]

nums_asc = bubble_sort(nums)
print('排序后的值：', nums_asc)

print()
"""
4.手写插入排序
实现插入排序函数 insertion_sort(arr)，原地排序。测试数据同上。
插入排序的思路：
从第二个元素开始，把它插入到前面已经排好序的部分。
一直重复，直到整个列表有序。
"""
def insertion_sort(arr_list):
    for i in range(1,len(arr_list)):
        key = arr_list[i]
        j = i - 1
        while j >= 0 and key < arr_list[j]:
            arr_list[j + 1] = arr_list[j]
            j-=1
            print(arr_list)
        arr_list[j + 1] = key
        print()


insertion_list = [5,3,8,4,2]

insertion_sort(insertion_list)
print('插入排序：',insertion_list)

print()
"""
5.线性查找与二分查找
编写两个函数：
linear_search(arr, target)：返回目标元素的索引，没找到返回 -1
binary_search(arr, target)：列表必须先排序，返回索引，没找到返回 -1
测试列表：[11, 12, 22, 25, 34, 64, 90]，查找 25 和 100。
"""

# 线性查找
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 二分查找
def binary_search(arr, target):
    left_index = 0
    right_index = len(arr) - 1
    find_index = -1
    # 最左边的位置要小于等于最右边的位置
    while left_index <= right_index:
        min = (left_index + right_index) // 2  # 中间值
        if arr[min] > target:
            right_index = min - 1
        elif arr[min] < target:
            left_index = min + 1
        else:
            find_index = min
            break
    return find_index


my_list = [11, 12, 22, 25, 34, 64, 90]
print('线性查找：', linear_search(my_list, 25))
print('线性查找：', linear_search(my_list, 100))

print('二分查找：', binary_search(my_list, 25))
print('二分查找：', binary_search(my_list, 100))

print()
"""
6.使用 bisect 模块
导入 bisect，实现：
在已排序列表中查找元素应该插入的位置（bisect_left）
向已排序列表中插入新元素并保持有序（bisect.insort）
初始列表 [1, 3, 4, 4, 7]，插入 4 和 5。
"""
import bisect

bisect_list = [1, 3, 4, 4, 7]
bisect.bisect_left(bisect_list, 4)
bisect.insort(bisect_list, 5)
print('bisect插入对应的值：', bisect_list)

"""
随机生成10个整数（1-100的范围）保存到列表，使用冒泡排序，对其进行从大到小排序
在第1题的基础上，使用二分查找，查找是否有8这个数，如果有，则返回对应的下标，如果没有，返回-1。

冒泡排序 加 二分查找
"""
import random

math_list = []
for num in range(10):
    math_list.append(random.randint(1, 100))

# print('随机生成的：', math_list)
# 冒泡排序
for i in range(len(math_list) - 1):
    for j in range(1, len(math_list) - i):
        if math_list[j - 1] > math_list[j]:
            math_list[j - 1], math_list[j] = math_list[j], math_list[j - 1]
print(math_list)


# 二分查找
def sort_list(my_list, find_val):
    left_index = 0;
    right_index = len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        min_index = (left_index + right_index) // 2  # 设置中间值
        if my_list[min_index] > find_val:
            right_index = min_index - 1
        elif my_list[min_index] < find_val:
            left_index = min_index + 1
        else:
            find_index = min_index
            break
    return find_index


print(sort_list(math_list, 8))
