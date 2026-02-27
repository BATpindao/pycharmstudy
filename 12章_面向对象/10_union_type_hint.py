"""
union联合类型注解
1.可以在变量，函数(方法)多可以使用union联合类型注解
2.使用union时，需要先导入 from typing import Union

基本语法：
Union[类型,类型,...]
Union[x,y]  Union[x,y]等价于 x|y 只要满足其中一个类型就可以
"""
from typing import Union

# 1.联合类型注解
n1: Union[int,str,list[int]] = [1,2,3]

# 2.联合容器类型注解
# n2是list类型，元素可以是int,str类型
n2:list[Union[int,str]] = [1,2,3,'qwe']

print()
# 3.函数/方法 使用联合类型注解
# 函数add 接收两个参数,参数的类型可以是int float, 返回值的类型可以是int float
def add(a:Union[int,float],b:Union[int,float])->Union[int,float]:
    return a+b

# 类型传的不对时会有黄色波浪线警告⚠️
print(add(1,2.0))

