class Person:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        # 加上__表示私有属性
        self.__owner = owner

    def show(self):
        print(self.name, self.age)

    # 加__表示私有方法
    def __kiss(self):
        print(self.__owner)
        print("kiss")

    def show_kiss(self):
        self.__kiss()


p = Person(name="", age=18, owner="张三")

p.show_kiss()
p.age = 10
print(p.age)
# 调用私有方法
p._Person__kiss()
# 调用私有属性
print(p._Person__owner)
# python中是是没有真正的私有机制的
