# _init__就是描述当前包信息的
# 一个包包含多个模块，一个模块包含多个功能

# 包含__init__.python的文件夹才算是包

# 包导入的方式
# import 包名.模块名
# from 包名 import 模块名
# from 包名 import *
# from 包名.模块名 import 功能名
# from 包名.模块名 import *
# import module1.my_fun
# from module1 import my_fun

# from module1.my_fun import out_line, out_line1

# from module1 import my_fun
from module1 import *

# 如果要导入包下所有模块，需要在__init__文件中添加__all__，指定模块

my_fun.out_line()
my_fun.out_line1()

from module1.my_fun import out_line
my_fun.out_line()
my_fun.out_line1()
