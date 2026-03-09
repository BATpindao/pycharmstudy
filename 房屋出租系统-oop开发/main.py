"""
1.主程序入口
2.创建house view 对象，显示主菜单
"""
from house_view import HouseView

if __name__ == '__main__':
    house = HouseView()
    house.main_menu()