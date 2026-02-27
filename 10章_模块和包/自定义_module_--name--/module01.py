# import hsp_hi
# import hsp_ok

"""
当一个python模块或包被导入时，__name__被设为模块的名称————通常为 python 文件本身的名称去掉 .py 后缀
而若模块是在顶层代码环境中执行，其中的__name__ 设为字符串 __mall__
"""
# hsp_hi.hi()
# hsp_hi.ok()
# print('--name--', __name__)


"""
使用 __all__可以控制 from 模块名 import* 时，哪些功能可以被导入，注意：import 模块名 方式，不受__all__的限制
"""

# from hsp_hi import *
from hsp_ok import *
ok()