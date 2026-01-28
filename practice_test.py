"""
冒泡排序🫧
"""
from traceback import print_tb

nums = [22, 55, 3, 88, 12, 22, -1, 0, -5]

for i in range(0, len(nums) - 1):
    for j in range(0, len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(f'第{i + 1}轮比较：{nums},比较的列表长度：{len(nums) - i - 1}')

print()
"""
顺序查找
"""


def seq_search(list_name, find_name):
    find_list = []
    for i in range(len(list_name)):
        if list_name[i] == find_name:
            print('找到了', find_name)
            find_list.append(i)
    if len(find_list) > 0:
        return find_list
    else:
        print('没有找到', find_name)
        return -1


list_name = ['白眉鹰王', '金毛狮王', '紫衫龙王', '青翼蝠王', '白眉鹰王']
find_index = '白眉鹰王'
print(seq_search(list_name, find_index))

print()
"""
二分查找：

函数名：def binary_search(my_list,find_val):
my_list: 一个有序的数组
find_val: 要找的值

第一步：定义左右边界 
left_index: 搜索范围的左边
right_index: 搜索返回的最右边
find_index: 返回值的下标
"""


def binary_search(my_list, find_val):
    left_index = 0
    right_index = len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        min_index = (left_index + right_index) // 2  # 设置中间值下标 求于数
        if my_list[min_index] > find_val:
            right_index = min_index - 1
        elif my_list[min_index] < find_val:
            left_index = min_index + 1
        else:
            find_index = min_index
            break

    return find_index


num_list = [1, 8, 10, 89, 1000, 1234]
print(binary_search(num_list, 1234))

print()
