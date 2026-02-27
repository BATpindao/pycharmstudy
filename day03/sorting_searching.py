"""
1.排序（Sorting）
    1.Python 内置排序方法（必须掌握，这些是最常用、最实用的）
        .sorted() 函数：返回新排序列表
        .list.sort() 方法：原地排序
        .关键参数：key（自定义排序规则）、reverse=True（降序）

    2.基础手工实现算法（至少掌握 2~3 种，理解思路最重要）
        .冒泡排序（Bubble Sort）
        .选择排序（Selection Sort）
        .插入排序（Insertion Sort）

    3.稍进阶但推荐了解的算法（理解分治思想）
        .归并排序（Merge Sort）
        .快速排序（Quick Sort）——Python 内置的 Timsort 就是基于它优化而来
"""
# 1. Python 内置排序方法（最常用，实际开发优先用这些）
"""
sorted函数(内置函数)
    .返回一个新的一排序列表，原列表不变
    .基本用法：sorted(可迭代对象,key=None,revere=False)
    
可迭代对象就是能被一个一个“挨个拿出来”的东西。
比如你有一个袋子，里面装着苹果、香蕉、橙子，你可以一个一个拿出来吃。这个袋子就像一个“可迭代对象”
"""
# 1.基本生序排序
sorted_nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = sorted(sorted_nums)  #生序 默认
print('生序：',sorted_nums)  #输出：[11, 12, 22, 25, 34, 64, 90]
print(sorted_nums) # 原列表不变 输出：[64, 34, 25, 12, 22, 11, 90]

# 2.降序排序
sorted_desc = sorted(sorted_nums,reverse=True)
print('降序：',sorted_desc)   # 输出：[90, 64, 34, 25, 22, 12, 11]

# 对字符串列表排序 (默认按字母顺序)
words = ['vivo','xiaomi','huawei','apple']
sorted_words = sorted(words)
print('字母升序：',sorted_words)  #生序 ['apple', 'huawei', 'vivo', 'xiaomi']
print('字母降序：',sorted(words,reverse=True)) #降序 ['xiaomi', 'vivo', 'huawei', 'apple']


print('===='*10)
"""
list.sort()方法
    .原地排序，直接修改原列表，返回 None。
    .用法：列表.sort(key=None, reverse=False)
"""
list_nums = [64, 34, 25, 12, 22, 11, 90]

list_nums.sort() #直接修改原列表
print('列表升序：',list_nums)
list_nums.sort(reverse=True)
print('列表降序：',list_nums)


print('===='*10)
"""
自定义排序（用 key 参数，最实用！）
当列表元素是复杂对象（如元组、字典）时，用 key 指定排序规则。
"""
students = [('Alice',85),('Boy',90),('charlie',78)]

#用sorted() 返回新列表
sorted_student = sorted(students,key=lambda x:x[1],reverse=True)
print('自定义排序规则：',sorted_student) #降序 lamda表达式

# 用list.sort()原地排序
students.sort(key=lambda x:x[1],reverse=False)
print('list.sort:',students) #升序

# 更复杂示例：列表中是字典，按 age 升序
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
people.sort(key=lambda x:x['age'])
print('年龄升序：',people)

print()
"""
2.查找（Searching）
    1.线性查找（Sequential/Linear Search）：最基础，适用于无序列表
    2.二分查找（Binary Search）：必须掌握，前提是列表已排序，效率高
    3.Python 内置工具
        .in 操作符、.index() 方法
        .bisect 模块（二分查找的标准库实现）：bisect_left、bisect_right、insort
"""
# 2. bisect 模块（高效二分查找和插入，列表必须已排序）查找
"""
import bisect
"""
import bisect
# 已排序列表
bisect_list = [1, 3, 4, 4,7]

# 查找插入的位置 (bisect_left:找到最左边的插入点)
pos = bisect.bisect_left(bisect_list, 4)
print(pos)                          # 输出: 2（插入到第2个4左边）

pos = bisect.bisect_left(bisect_list, 5)
print(pos)                          # 输出: 4（插入到7前面）

# 实际插入并保持有序（insort）
bisect.insort(bisect_list, 5)       # 插入5
print(bisect_list)                  # 输出: [1, 3, 4, 4, 5, 7]

bisect.insort_left(bisect_list, 4)  # 插入到最左边
print(bisect_list)                  # 输出: [1, 3, 4, 4, 4, 5, 7]

print()
"""
3. 手写基础算法（理解原理，面试常用）
冒泡排序（bubble_sort）
每次比较相邻元素，大的往后“冒泡”。
"""
def bubble_sort(arr):
    n = len(arr)
    new_arr = arr[:]                # 复制一份，不要修改原列表
    for i in range(n):
        for j in range(n - i - 1):
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr

# 测试
nums = [5, 3, 8, 4, 2]
print('冒泡排序：',bubble_sort(nums))            # 输出: [2, 3, 4, 5, 8]
print(nums)                         # 原列表不变


print()
"""
插入排序（insertion_sort，原地）
像打扑克牌一样，逐个插入到前面已排序部分。
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr                      # 已原地修改

# 测试
nums = [5, 3, 8, 4, 2]
insertion_sort(nums)
print('插入排序：',nums)                         # 输出: [2, 3, 4, 5, 8]

print()
# 4. 查找方法  内置简单查找
nums = [11, 12, 22, 25, 34, 64, 90]

# in 操作符
print(25 in nums)                   # True

# index() 方法（没找到会报错）
print(nums.index(25))               # 3
# print(nums.index(100))            # 会报 ValueError

# 手写线性查找
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(nums, 25))       # 3
print(linear_search(nums, 100))      # -1


# 手写二分查找（列表必须已排序）
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_nums = [11, 12, 22, 25, 34, 64, 90]
print(binary_search(sorted_nums, 25))   # 3
print(binary_search(sorted_nums, 100))  # -1

"""
要掌握的东西
    1.核心能力
        .能用内置方法快速完成排序和查找任务（实际开发 90% 都用内置）
        .能手写冒泡、插入、二分查找等基础算法（面试常见）
        .理解每种算法的时间复杂度（平均/最坏情况）和空间复杂度
        .知道算法的适用场景：小数据用简单算法，大数据用高效算法
        .能用 key 参数处理复杂对象排序（如列表中字典按某个键排序）
"""
"""
算法,平均时间复杂度,最坏时间复杂度,空间复杂度,稳定
冒泡排序,O(n²),O(n²),O(1),稳定
选择排序,O(n²),O(n²),O(1),不稳定
插入排序,O(n²),O(n²),O(1),稳定
归并排序,O(n log n),O(n log n),O(n),稳定
快速排序,O(n log n),O(n²),O(log n),不稳定
Python 内置,O(n log n),O(n log n),O(n),稳定
线性查找,O(n),O(n),O(1),-
二分查找,O(log n),O(log n),O(1),-
"""

