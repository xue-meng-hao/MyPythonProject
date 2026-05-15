class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 继承，在小括号中写入父类名字
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school


class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        print('%s正在以%s的时速行驶' % (self.name, self.speed))


class Bus(Car):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        # 调用父类的方法：以下两种是等价的
        super().run()
        Car.run(self)
        self.capacity = capacity

    def run(self):
        print('%s正在以%s的时速行驶, 载客量是%s' % (self.name, self.speed, self.capacity))


class Taxi(Car):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        self.capacity = capacity

    def run(self):
        print('%s正在以%s的时速行驶, 载客量是%s' % (self.name, self.speed, self.capacity))


bus1 = Bus("blue", 3, 15)
bus1.run()
taxi1 = Taxi("yellow", 4, 5)
taxi1.run()
