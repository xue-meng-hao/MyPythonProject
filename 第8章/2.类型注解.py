from typing import Union

# 旧版本的没有|的写法,使用Union[]来实现
hobby: list[Union[str, int]] = ["cricket", 10]
print(hobby)
hobby: list[str | int] = ["cricket", 10]
print(hobby)
hobby.append("football")
print(hobby)
# 集合指定类型
cities: set[str] = {"北京", "上海", "深圳"}
cities.add("广州")
print(cities)
# 字典指定类型
students: dict[int, str] = {1: '张三', 2: '李四'}
students.update({3: '王五'})
students.update({1: '张三丰'})
students.update({5: '王五'})
print(students)
# 元组指定类型
names1: tuple[str] = ("张三",)
print(names1)
# 元组是有多少元素指定多少个类型
names2: tuple[str, str, int] = ("张三", "李四", 190)
print(names2)
# 若类型一致可以使用...来替代
names3: tuple[str, ...] = ("张三", "李四", "王五")
print(names3)


# 对函数的参数进行类型注解,使用参数名:类型,返回值使用->类型
def add(*args: int | float) -> int | float:
    return sum(args)
