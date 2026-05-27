# import math
#
# print(math.ceil(3.5))
#
# import random
#
# print(random.randint(1, 10))
#
# import time
# # import datetime as dt
# # print(dt.datetime.now())
# # print(datetime.datetime.today())
# # print(datetime.date.today())
# # 导入模块功能名
# from datetime import datetime as dt
# from random import randint as rnd
#
# print(f"测试：{dt.now()}")
# for i in range(10):
#     print(f"测试的随机数：{rnd(1, 10)}")

# __name__制定方法名,是一个动态值,如果直接执行是使用main,若引用了其他模块,则是打印模块名
# __all__制定导入模块*的功能


# from module1.test import *
# from module1.test import age
#
# print(name)
# print(age)

import module1.test
# print(__name__)

# if __name__ == '__main__':
#     print("我是主程序")
