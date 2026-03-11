"""
业务层：
1.编写HouseService类
2.提供方法完成对房屋的各种操作
增删查改（crud）
"""
from house import *

class HouseService:
    # 初始化的一些用户信息
    __houses:list[House] = []
    id_count = 0
    def __init__(self):
        h = House(1, 'tim', '123', '海淀', 800, '未出租')
        self.__houses.append(h)
        self.id_count = len(self.__houses)
    def get_index_count(self):
        return len(self.__houses)

    def insert_house(self,house:House):

        self.__houses.append(house)
    # 新增用户数据
    def add(self,house_info:House):
        self.__houses.append(house_info)

    # 查询所有房屋信息
    def list_houses(self):
        return self.__houses

    #按ID查找
    def find_by_id(self,house_id:int)->House:
        for house in self.__houses:
            if house.id == house_id:
                return house

    #删除房屋信息
    def del_house(self,house:House):
        self.__houses.remove(house)

    # 修改房屋信息
    def update_house(self,house_id:int,name:str,phone:str,address:str,rent:int,state:str):
        is_house = self.find_by_id(house_id)
        if is_house:
            # 修改赋值
            is_house.name = name
            is_house.phone = phone
            is_house.address = address
            is_house.rent = rent
            is_house.state = state
            return is_house


