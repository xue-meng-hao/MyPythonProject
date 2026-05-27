# 以__xx__命名的特殊方法（双下划线开头和结尾）
# 常用魔法方法：
# __str__
# __len__
# __lt__
# __gt__ 小于
# __eq__ 等于，默认使用的是内存地址
# __ne__ 不等于
# __getattr__ 访问不存在的属性时


# __init__
# __new__
# __call__
# __del__
# __repr__
# __setattr__
class Persion:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "名字是{},年龄是{}".format(self.name, self.age)

    def __len__(self):
        # return self.__dict__.__len__()
        return len(self.__dict__)

    def __getattribute__(self, name):
        return "您访问的属性不存在"


p11 = Persion("P11", 10, "male")
print(p11)
print(str(p11))
print(len(p11))

print(p11.address)

print(issubclass(Persion, object))
print(isinstance(p11, object))
print(isinstance(11, object))
print(isinstance(11.6, object))

# 对象可以访问到的东西（包括自己的和继承过来的）
print(dir(object))
