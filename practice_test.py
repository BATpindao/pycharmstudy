"""
冒泡排序🫧
"""
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


list_name = ['白眉鹰王', '金毛狮王', '紫衫龙王', '青翼蝠王','白眉鹰王']
find_index = '白眉鹰王'
print(seq_search(list_name, find_index))
