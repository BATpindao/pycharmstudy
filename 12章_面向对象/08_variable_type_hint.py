# 类型注解的使用
"""
1.基础数据类型注解

n1:int = 10 解读：
1.n1:int:对n1 进行类型注解，标注n1 的类型为int
2.注意如果，给出的值和标注的类型不一致，则pycharm会给出黄色的警告
"""
n1: int = 10
n2: str = 'abc'
n3: float = 3.14
is__pass: bool = True

"""
2.示例对象类型注解
"""
class Cat:
    pass

class Dog:
    pass

# 实例对象类型注解
# c:Cat :对cat类型进行类型注解，标注cat的类型是Cat
# c:Cat = Dog()
c: Cat = Cat()

"""
3.容器类型注解

my_list:list:对my_list进行了类型注解，将my_list的类型标注成了 list 类型
"""
my_list:list = [1, 2, 3]
my_tuple:tuple = (1, 2, 3)
my_set: set = {1,2,3,4}
my_dict:dict = {'1':1, '2':2, '3':3}

"""
4.容器详细类型注解
"""
my_info_list:list[int] = [1,2,3,4]
# 元组类型，设置详细类型注解时，需要把每个元素的类型都标注一下
my_info_tuple:tuple[str,str,str,int] = ('anna','jek','tom',4)
my_info_set:set[str] = {'1','2','3'}

# 字典类型的详细注解设置时，需要设置两个属性 [key,value] 都需要设置一下类型
my_info_dict:dict[str, int] = {'1':1,'2':2,'3':3}

"""
5.注释中使用注解

语法： # type:类型 [详细注解类型(容器注解中使用要带)]
"""
a = 10 # type:int
a_list = [1,2,3,4] # type:list[int]
