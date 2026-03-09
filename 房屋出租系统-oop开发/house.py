"""
数据层
house类
一个对象即表示一个房屋信息对象
"""

class House:
    id:int = None
    name:str = None
    phone:str = None
    address:str = None
    rent:int = None
    state:str = None

    def __init__(self, id, name, phone, address, rent, state):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rent = rent
        self.state = state

    def __str__(self):
        return f'{self.id}  {self.name}  {self.phone}  {self.address}   {self.rent}     {self.state}'
