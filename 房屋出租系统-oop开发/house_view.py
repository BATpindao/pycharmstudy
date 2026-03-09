"""
界面层：house_view
1.编写类：HouseView
2.显示界面
3.接收用户输入
4.调用业务方法完成对房屋的各种操作
"""
from house_service import HouseService
from utility import Utility

class HouseView:
    def __init__(self):
        self.house_service = HouseService()

    # 显示主菜单
    def main_menu(self):
        while True:
            print('房屋出租系统菜单'.center(40, '='))
            print(' 1 新 增 房 源'.center(40))
            print(' 2 查 找 房 源'.center(40))
            print(' 3 删 除 房 屋 信 息'.center(44))
            print(' 4 修 改 房 屋 信 息'.center(44))
            print(' 5 房 屋 列 表'.center(40))
            print('6 退 出'.center(38))
            index = int(input('请输入你的选择(1-6):'))

            match index:
                case 1:
                    self.add_house()
                case 2:
                    self.find_house()
                case 3:
                    self.del_house()
                case 4:
                    self.update_house()
                case 5:
                    self.list_houses()
                    pass
                case 6:
                    is_ok = Utility.read_confirm_select()
                    if is_ok:
                        print('你退出了程序，欢迎下次使用。。')
                        break
                case _:
                    print('请输入系统中存在的功能')

        pass

    # 添加房屋信息
    def add_house(self):
        print('添加房屋信息'.center(31, '='))
        name = input('姓名：')
        phone = input('电话：')
        address = input('地址：')
        rent = int(input('租金：'))
        state = input('状态：')
        house = {'id': self.house_service.id_count+1, 'name': name, 'phone': phone, 'address': address, 'rent': rent, 'state': state}
        self.house_service.add(house)
        # 有系统分配添加的房屋ID
        print('添加房屋成功'.center(31, '='))

    # 展示房屋列表
    def list_houses(self):
        print('房屋列表'.center(60, '='))
        print('编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（未出租/已出租）')
        list_house = self.house_service.list_houses()
        for house in list_house:
            for value in house.values():
                print(value, end='\t\t')
            print()

        print('房屋列表显示完毕'.center(60, '='))

    # 更具ID查找房屋信息
    def find_house(self):
        print('查找房屋信息'.center(31, '='))
        house_id = int(input('请输入要查找的ID：'))
        # 这里要调用业务类的查找
        house = self.house_service.find_by_id(house_id)
        if house:
            print('编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（未出租/已出租）')
            for value in house.values():
                print(value, end='\t\t')
            print()
        else:
            print(f'查找的房屋信息ID{house_id}不存在'.center(31, '='))

    #删除房屋信息
    def del_house(self):
        while True:
            print('删除房屋信息'.center(31, '='))
            house_id = int(input('请输入带删除的房屋编号(-1退出)：'))
            if house_id == -1:
                print('删除房屋信息，退出成功')
                break
            #判断是否进入下一步 删除房屋信息要调用业务类
            is_show = Utility.read_confirm_select()
            if is_show:
                # 开始删除房屋信息 调用业务类
                is_house = self.house_service.find_by_id(house_id)
                if is_house:
                    # 执行删除操作 调用业务类
                    self.house_service.del_house(is_house)
                    print('删除房屋信息成功'.center(31, '='))
                    break
                else:
                    print('房屋编号不存在，删除失败(请选择存在的房屋编号)'.center(31, '='))

    # 修改房屋信息
    def update_house(self):
        print('修改房屋信息'.center(31, '='))
        while True:
            house_id = int(input('请选择带修改房屋的编号（-1表示退出）:'))
            if house_id == -1:
                break
            else:
                # 判断用户是否存在
                is_house = self.house_service.find_by_id(house_id)
                if is_house:
                    name = input(f'姓名({is_house['name']}):')
                    phone = input(f'电话({is_house['phone']}):')
                    address = input(f'地址({is_house['address']}):')
                    rent = input(f'租金({is_house['rent']}):')
                    state = input(f'状态({is_house['state']}):')

                    # 修改赋值
                    is_house['name'] = name
                    is_house['phone'] = phone
                    is_house['address'] = address
                    is_house['rent'] = rent
                    is_house['state'] = state

                    print('修改房屋信息成功'.center(31, '='))
                    break
                else:
                    print('房屋编号不存在，请重新选择'.center(31, '='))
                    break


