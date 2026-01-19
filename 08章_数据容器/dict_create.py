"""
字典生成式
    内置函数zip()
    zip()可以将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，返回由这些元组组成的列表。
    字典生成式基本语法：

        {字典 key 的表达式: 字典 value 的表达式 for 表示 key 的变量, 表示 value 的变量 in zip(可迭代对象, 可迭代对象)}
        可迭代对象1 = [1,2]
        可迭代对象2 = [3,4]
        {key:value for key,value in zip(可迭代对象1,可迭代对象2)}
"""

# 字典。没有对应的值化就不组成字典
english_list = ['red', 'black', 'yellow', 'white']
chinese_list = ['红色', '蓝色', '黄色', '白色', '绿色']

print({key.upper(): value for key, value in zip(english_list, chinese_list)})

print()
clerks = {
    "0001": {
        "age": 20,
        "name": "贾宝玉",
        "entry_time": "2011-11-11",
        "salary": 12000
    },
    "0002": {
        "age": 21,
        "name": "薛宝钗",
        "entry_time": "2015-12-12",
        "salary": 10000
    },
    "0010": {
        "age": 18,
        "name": "林黛玉",
        "entry_time": "2018-10-10",
        "salary": 20000
    }
}

print('0010员工的信息：', clerks['0010'])

# 添加/删除 员工
# 添加
clerks['0020'] = {
    'age': 30,
    'name': '老韩',
    'entry_time': '2020-08-10',
    'salary': 6000
}
print('添加员工', clerks)
#  删除
del clerks['0001']  # 删除 0001 会影响原来的字典
print('删除员工：', clerks)

# 修改员工信息

clerks['0020']['name'] = '韩顺平'
clerks['0020']['entry_time'] = '1999 - 10 - 10'
clerks['0020']['salary'] = float(clerks['0020']['salary']) + float(clerks['0020']['salary']) * 0.1

print('修改后的信息：',clerks['0020'])

# 要求：遍历所有员工，把所有员工的薪水，在原工资的基础上，增加20%
for key in clerks:
    clerks[key]['salary'] = clerks[key]['salary']+clerks[key]['salary']*0.2
    print(clerks[key])

"""
比较项	                列表（list）	        元组（tuple）	        字符串（str）	        集合（set）	        字典（dict）
是否支持多个元素	            Y	                Y	                      Y	                Y	                Y
元素类型	                    任意	                任意	                      只支持字符	        任意	                Key：通常是字符串或数字 Value：任意
是否支持元素重复	            Y	                Y	                      Y	                N	                Key 不能重复  Value 可以重复
是否有序	                    Y	                Y	                      Y 	            N	                3.6 版本之前是无序的  3.6 版本之后开始支持元素有序
是否支持所有	                Y	                Y	                      Y	                N	                N
可修改性/可变性	            Y	                N	                      N	                Y	                Y
使用场景	               可修改、可重复的多个数据	    不可修改、可重复的多个数据	  字符串	        不可重复的多个数据	        通过关键字查询对应数据的需求
定义符号	                    []	                ()	                      "" 或 ''	        {}	                 {key: value}
"""
