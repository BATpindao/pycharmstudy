def hi():
    print('shp hi')

def ok():
    print('shp ok')

print('hsp_ok--name--',__name__)


"""
1.在 module01.py 中，没有 __all__时，会导入所有的功能
2.使用了__all__ = ['ok'] 在其他文件使用 form module01 import * 只会导入ok()
3.注意：import 模块 方式，不受 __all__ 限制
"""
__all__ = ['ok']