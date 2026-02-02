"""
导包基本语法：
    import 包名.模块  使用：包名.模块.功能
    from 包名 import 模块   使用：模块.功能，不用带包名
"""
from math import fabs

# 方式一：import 包名.模块
# import hsp_package.module01 as module01
# import hsp_package.module02 as module02
#
# module01.hi()
# module02.ok()

# 方式二：from 包名 import 模块
# from hsp_package import module01
# from hsp_package import module02
#
# module01.ok()
# module02.ok()

"""
导入包的模块的指定函数、类、变量 
基本语法：
    from 包名.模块 import 函数、类、变量
1.上面是导入包的模块的指定函数、类、变量
2.在使用时，直接调用功能
3.from 包名.模块 import * ：表示导入包的模块的所有功能
"""
# module01单个函数引入,module02全部引入
# from hsp_package.module01 import hi
# from hsp_package.module02 import *
# hi()
# ok()


"""
1.__init__.py 通过 __all__ = [允许导入的模块列表]
2.针对from 包 import * 方式生效 ， 对 import xx 方式不生效
"""
# from hsp_package.module02 import *
# 导入这个包下的所有模块
# from hsp_package import *
# # hi()
# module02.ok()

"""
1.包中还可以创建包
2.在使用时，通过 . 来确定层级关系
"""
# 方式一
# import hsp_package.hsp_package02.module03
# # 使用
# hsp_package.hsp_package02.module03.cal(2,3)

# 方式二 直接使用
# from hsp_package.hsp_package02.module03 import cal
# cal(5,7)

#方式三
from  hsp_package.hsp_package02 import module03
module03.cal(1,2)

print(fabs(-1992))