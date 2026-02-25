"""
1.函数（方法）的类型注解

基本语法：
    def 函数/方法名(行参名:类型,行参名:类型....) -> 返回类型:
        函数/方法体

1. name: str 对形参name进行类型注解: 标注name类型是str
2. 在调用方法/函数时，传入的实参类型不是一样的，则给出黄色的警告
"""


def fj_str(i: str):
    for a in i:
        print(a)

fj_str('qwe')

print()
"""
2.对函数方法 返回值类型进行注解
"""
def add(a:int,b:int) ->int:
    return a+b

print(add(1,2))

"""
注意：
类型注解是提示的，并不是强制性的，如果你给定的类型和标注的类型不一致，pycharm只会给一个黄色的警告，代码依然可以运行
"""