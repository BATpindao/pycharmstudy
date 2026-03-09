"""
业务层：
1.编写HouseService类
2.提供方法完成对房屋的各种操作
增删查改（crud）
"""

class HouseService:
    # 初始化的一些用户信息
    __houses:list[dict] = [{'id':1,'name':'tim','phone':'113','address':'海淀','rent':800,'state':'未出租'}]
    id_count = len(__houses)

    # 新增用户数据
    def add(self,house_info:dict):
        self.__houses.append(house_info)

    # 查询所有房屋信息
    def list_houses(self):
        return self.__houses

    #按ID查找
    def find_by_id(self,house_id:int)->dict:
        for house in self.__houses:
            if house['id'] == house_id:
                return house

    #删除房屋信息
    def del_house(self,house:dict):
        self.__houses.remove(house)

    # 修改房屋信息
    def update_house(self,house_id:int,name:str,phone:str,address:str,rent:int,state:str):
        is_house = self.find_by_id(house_id)
        if is_house:
            # 修改赋值
            is_house['name'] = name
            is_house['phone'] = phone
            is_house['address'] = address
            is_house['rent'] = rent
            is_house['state'] = state
            return is_house


