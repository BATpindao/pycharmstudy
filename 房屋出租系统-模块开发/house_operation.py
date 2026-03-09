"""
说明：提供对房屋的给种操作 CRUD
"""
from my_tools import *

# 全局变量 houses 存放所有的房屋信息
houses = [{'id':1,'name':'tim','phone':'113','address':'海淀','rent':800,'state':'未出租'}]

# 全局变量id_counter 记录当前房屋的ID
id_count = len(houses)

# 删除房屋信息
def del_house():
    """
    删除房屋信息
    :return:
    """
    while True:
        print('删除房屋信息'.center(31,'='))
        house_id = int(input('请输入带删除的房屋编号(-1退出)：'))
        if house_id == -1:
            print('删除房屋信息，退出成功')
            break
        # 判断是否进入下一步
        is_show = read_confirm_select()
        if is_show:
            # 开始删除房屋信息
            is_house = find_by_id(house_id)
            if is_house:
                # 执行删除操作
                houses.remove(is_house)
                print('删除房屋信息成功'.center(31,'='))
                break
            else:
                print('房屋编号不存在，删除失败(请选择存在的房屋编号)'.center(31,'='))

# 更具房屋ID查出除房屋出租信息
def find_by_id(find_id:int) -> dict:
    """
    更具输入的find_id返回对应的房屋信息字典，如果没有就返回None
    :param find_id:
    :return:
    """
    for house in houses:
        if house['id'] == find_id:
            return house

# 更具ID查找房屋信息
def find_house():
    print('查找房屋信息'.center(31,'='))
    house_id= int(input('请输入要查找的ID：'))
    house = find_by_id(house_id)
    if house:
        print('编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（未出租/已出租）')
        for value in house.values():
            print(value,end='\t\t')
        print()
    else:
        print(f'查找的房屋信息ID{house_id}不存在'.center(31,'='))

# 展示所有的房屋出租信息
def list_houses():
    """
    显示房屋列表
    :return:
    """
    print('房屋列表'.center(60,'='))
    print('编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（未出租/已出租）')
#    遍历houses这个列表
    for house in houses:
        # 循环字典
        for value in house.values():
            print(value,end='\t\t')
        # 输出完一个完整的house信息 换行
        print()
    print('房屋列表显示完毕'.center(60,'='))

# 添加房屋信息
def add_house():
    """
    添加房屋信息
    :return:
    """
    print('添加房屋信息'.center(31,'='))
    name = input('姓名：')
    phone = input('电话：')
    address = input('地址：')
    rent = int(input('租金：'))
    state = input('状态：')
    #有系统分配添加的房屋ID
    global id_count #当函数內想要使用全局变量时 要加一下global
    id_count += 1

    # 构建房屋信息对应的字典，加入到全局houses列表中
    house = {'id':id_count,'name':name,'phone':phone,'address':address,'rent':rent,'state':state}
    houses.append(house)
    print('添加房屋成功'.center(31,'='))

# 修改房屋信息
def update():
    print('修改房屋信息'.center(31,'='))
    while True:
        house_id = int(input('请选择带修改房屋的编号（-1表示退出）:'))
        if house_id == -1:
            break
        else:
            is_house = find_by_id(house_id)
            if is_house:
                # name = input(f'姓名({is_house['name']}):')
                # phone = input(f'电话({is_house['phone']}):')
                # address = input(f'地址({is_house['address']}):')
                # rent = input(f'租金({is_house['rent']}):')
                # state = input(f'状态({is_house['state']}):')
                # 进阶写法，用户直接回车也没事
                name = input(f'姓名({is_house["name"]}):') or is_house["name"]
                phone = input(f'电话({is_house["phone"]}):') or is_house["phone"]
                address = input(f'地址({is_house["address"]}):') or is_house["address"]
                rent = input(f'租金({is_house["rent"]}):') or is_house["rent"]
                state = input(f'状态({is_house["state"]}):') or is_house["state"]
                # 修改赋值
                is_house['name'] = name
                is_house['phone'] = phone
                is_house['address'] = address
                is_house['rent'] = rent
                is_house['state'] = state

                print('修改房屋信息成功'.center(31,'='))
                break
            else:
                print('房屋编号不存在，请重新选择'.center(31,'='))
                break


# 退出房屋租令系统
def exit_sys():
    return read_confirm_select()

#显示主菜单
def main_menu():
    """
    显示主菜单，让用户选择
    :return:
    """
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
                add_house()
            case 2:
                find_house()
            case 3:
                del_house()
            case 4:
                update()
            case 5:
                list_houses()
            case 6:
                is_ok = exit_sys()
                if is_ok:
                    print('你退出了程序，欢迎下次使用。。')
                    break
            case _:
                print('请输入系统中存在的功能')

# 测试
if __name__ == '__main__':
    del_house()
    pass