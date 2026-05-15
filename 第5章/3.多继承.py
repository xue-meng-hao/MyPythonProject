class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        print('%s正在以%d的时速行驶' % (self.name, self.speed))


class HuaweiDriving:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        print('huawei:%s正在以%d的时速行驶' % (self.name, self.speed))

    def huawei_run(self):
        print('huawei_run:%s正在以%d的时速行驶' % (self.name, self.speed))


# 多继承默认有限使用第一个父类的同名属性和方法
class WenjieDriving(HuaweiDriving, Car):
    def __init__(self, name, speed, version: int = 10):
        super().__init__(name, speed)
        self.version = version

    def run(self):
        print('%s正在以%d的时速行驶,版本:%s' % (self.name, self.speed, self.version))


wenjie = WenjieDriving('问界', 100)
wenjie.run()
wenjie.huawei_run()
# 使用mro查看继承关系
print(WenjieDriving.__mro__)


def run(car: Car):
    car.run()


# 多态，子类对象可以作为父类的引用
run(WenjieDriving('问界', 100))
run(Car('新车', 100))
