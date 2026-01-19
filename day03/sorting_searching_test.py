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
print('sort 降序',sort_list)


print()
"""
2.自定义排序
有列表 students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]，按成绩从高到低排序（成绩是第二个元素）。
"""
students =[('Alice',85),('Bob',92),('Charlie',78)]
students.sort(key=lambda x:x[1], reverse=True)
print('降序：',students)


print()
"""
3.手写冒泡排序
实现冒泡排序函数 bubble_sort(arr)，返回排序后的新列表（不要修改原列表）。测试数据：[5, 3, 8, 4, 2]。
"""
def bubble_sort(arr):
    n = len(arr)
    new_arr = arr[:] #重新创建一份新的
    for i in range(n):
        for j in range(n - i - 1):
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr

nums = [5, 3, 8, 4, 2]

nums_asc = bubble_sort(nums)
print('排序后的值：',nums_asc)

print()
"""
4.手写插入排序
实现插入排序函数 insertion_sort(arr)，原地排序。测试数据同上。
插入排序的思路：
从第二个元素开始，把它插入到前面已经排好序的部分。
一直重复，直到整个列表有序。
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):       # 从第二个元素开始
        key = arr[i]                   # 当前要插入的元素
        j = i - 1                      # 从前面往回看
        while j >= 0 and arr[j] > key: # 如果前面的比它大，就往后挪
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key               # 插入到合适位置
    return arr

# 测试
nums = [5, 3, 8, 4, 2]
insertion_sort(nums)
print("插入排序：", nums)   # 输出: [2, 3, 4, 5, 8]


"""
5.线性查找与二分查找
编写两个函数：
linear_search(arr, target)：返回目标元素的索引，没找到返回 -1
binary_search(arr, target)：列表必须先排序，返回索引，没找到返回 -1
测试列表：[11, 12, 22, 25, 34, 64, 90]，查找 25 和 100。
"""



print()
"""
6.使用 bisect 模块
导入 bisect，实现：
在已排序列表中查找元素应该插入的位置（bisect_left）
向已排序列表中插入新元素并保持有序（bisect.insort）
初始列表 [1, 3, 4, 4, 7]，插入 4 和 5。
"""
import bisect
bisect_list = [1,3,4,4,7]
bisect.bisect_left(bisect_list, 4)
bisect.insort(bisect_list, 5)
print('bisect插入对应的值：',bisect_list)
