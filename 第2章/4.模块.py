import math

print(math.ceil(3.5))

import random

print(random.randint(1, 10))

import time
# import datetime as dt
# print(dt.datetime.now())
# print(datetime.datetime.today())
# print(datetime.date.today())
# 导入模块功能名  
from datetime import datetime as dt
from random import randint as rnd

print(f"测试：{dt.now()}")
for i in range(10):
    print(f"测试的随机数：{rnd(1, 10)}")

# __name__制定方法名
# __all__制定导入模块*的功能
