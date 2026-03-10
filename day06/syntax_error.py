"""
错误异常：
1.什么事错误 (ERROR)
    错误就是程序运行时出现的问题
"""
# print(10/0) #运行时报错(runtime error)： (除数不能为0)ZeroDivisionError: division by zero

"""
2.常见的python异常类型
学习python时最常见的几个异常类型：
| 异常类型                | 含义       | 示例             |
| ------------------- | -------- | -------------- |
| `ZeroDivisionError` | 除0错误     | `10/0`         |
| `NameError`         | 变量未定义    | `print(a)`     |
| `TypeError`         | 类型错误     | `"10" + 5`     |
| `ValueError`        | 值错误      | `int("abc")`   |
| `IndexError`        | 索引越界     | `list[10]`     |
| `KeyError`          | 字典key不存在 | `dict["name"]` |
| `FileNotFoundError` | 文件不存在    | 打开不存在文件        |
"""

"""
3.异常处理（try-except）
使用 try-except来捕获错误
语法：
    try:
        （代码流程）可能出错的代码
    except:
        出错后执行
"""
try:
    print(10/0)
except:
    # 这样处理程序不会蹦，增加了容错性
    print('程序异常了')


"""
4.捕获指定异常（推荐）

"""
try:
    print(10/0)
    # print(a)
except ZeroDivisionError:
    # 可以针对不同的错误进行处理
    print('除数不能为0')
except NameError:
    print('变量为定义')

"""
5.获取异常信息
"""
try:
    num1 = int('qwe')
except Exception as e:
    # 输出错误信息
    print(e)

print()
"""
6.finally(一定执行)

finally不管有没有错误都会执行
常用于：
    。关闭文件
    。关闭数据库
    。释放资源
"""
try:
    f =open('aa.txt')
    print(f.read())
except FileNotFoundError as e:
    print('文件不存在')
finally:
    print('程序执行结束')


print()
"""
7.完整结构
python 完整异常结构：
try:
    可能出错代码
except 错误类型:
    处理代码
else:
    没有错误执行
finally:
    一定执行
"""
try:
    # abc = int(input('输入数字:'))
    abc = int('qwe')
except ValueError as e:
    print('输入的不是数字')
else:
    print('输入正确')
finally:
    print('程序执行结束')


print()
"""
8.主动抛出异常（raise）
程序猿可以自己制造异常
"""
# age = int(-1)
#
# if age < 0:
#     raise ValueError("年龄不能为负数")

"""
9.自定义异常（进阶）
自定义异常类要继承Exception
"""
# class AgeError(Exception):
#     pass
#
# age = -1
# if age < 0:
#     raise AgeError('年龄不能小于0')

print()
"""
10.程序员实际写法(最常用)

一般会用：Exception 因为他可以捕获所有的异常
"""
try:
    result = 10/0
except Exception as e:
    print('程序错误：',e)


print()
"""
11.学习异常最重要理解：
异常的目的不是避免错误，而是让程序在出错时还能继续执行

例如：
用户输入错误：
    请输入年龄: abc
如果没有异常处理：
    程序直接崩溃
如果有异常：
    输入错误，请重新输入
"""

"""
12.异常错误非常重要的三点知识：
1.raise (主动抛异常)
    程序员自己制造异常
    if 1<0:
        raise ValueError('年龄不能为负数')
        
2.自定义异常
class Age(Exception):
    pass
    
3.finally (资源释放)
file.close()
"""
