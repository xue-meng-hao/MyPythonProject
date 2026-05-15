# 函数必须先定义再调用
# 函数定义不会执行，调用才会执行
# 函数通过缩进描述归属关系
import math


def out_line():
    print("---------")


out_line()


def circle_area(radius):
    """
    函数文档：使用三引号直接使用
    :param radius: 半径
    :return: 面积
    """
    area = math.pi * radius * radius
    return area


c_area = circle_area(10)
print(f"{c_area:.2f}")


def circle_area_len(radius):
    """
    获取面积和周长
    :param radius: 半径
    :return: 面积和周长
    """
    area = math.pi * radius * radius
    len = 2 * math.pi * radius
    return round(area, 1), round(len, 2)


area_len = circle_area_len(10)
print(type(area_len))
print(area_len)
area, len = area_len
print(area)
print(len)
# print(f"{area_len[0]:.2f},{area_len[1]:.2f}")

help(print)
