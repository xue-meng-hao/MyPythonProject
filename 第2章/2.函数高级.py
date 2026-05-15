num = 10


def test():
    global num
    num = 100
    print(num)


test()
print(num)


# 可以制定默认值
def reg_stu(name, age, gender, city: str = "北京"):
    print(f"姓名：{name},年龄：{age},性别：{gender},城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 关键字参数
stu = reg_stu(name="test", city="上海", gender="男", age=20)
print(stu)
# 位置参数
stu = reg_stu("test1", 18, "男", "杭州")
print(stu)
# 关键字参数和位置参数混合
stu = reg_stu("test1", 18, city="北京", gender="女")
print(stu)

stu = reg_stu("测试1", 18, "男")
print(stu)


# 不定长参数，多个参数会封装为一个元组
def calc_data(*args):
    print(type(args))
    print(args)


calc_data(1, 2, 3, 4)


def calc_sum(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    print(kwargs["a"])


calc_sum(2, 3, a="test")
