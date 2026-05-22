class Person:
    def __init__(self, name, age, idcard):
        self.name = name  # 公有属性，当前类中，子类中，类外部都可以访问
        self._age = age  # 保护属性，当前类中，子类中可以访问，类外部不可以访问
        self.__idcard = idcard  # 私有属性，当前类中，子类中，类外部都不可以访问

    @property
    def age(self):
        return self._age

    # def set_age(self, age):
    #     if isinstance(age, int) and 0 < age < 120:
    #         self._age = age
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 0 < age < 120:
            self._age = age

    # 使用装饰器实现私有属性的访问
    @property
    def idcard(self):
        return self.__idcard


# persion = Person("张三", 20, "123456789")
# print(persion.name)
# print(persion._age)
# print(persion.__idcard)


# class Student(Person):
#     def hello(self):
#         print(f"我{self.name}的年龄是{self._age}，身份证号码是{self.__idcard}")
#
# student = Student("李四", 21, "987654321")
# student.hello()

p = Person("王五", 22, "123456789")
# print(p.name)
# print(p._age)  # 类外部强制访问仍可访问到，但是不推荐
# print(p.__idcard)  # 类外部强制访问私有属性，报错

print(p.__dict__)

# python底层是通过重命名的方式实现的私有属性
# print(p._Person__idcard)
#
# print(p.get_age())
#
# print(p.idcard)
#
# print(p.get_age())
# p.set_age(23)
# print(p.get_age())


print(p.age)
p.age = 20
print(p.age)

# python的setter和getter通过装饰器@property实现getter方法，@age.setter装饰器实现setter方法
