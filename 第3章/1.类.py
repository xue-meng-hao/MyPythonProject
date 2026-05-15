class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


car = Car(1, 2)
print(car.__dict__)
print(car.make)
print(car.model)


class Car1:
    pass


car1 = Car1()
print(car1.__dict__)
car1.color = "red"
car2 = Car1()
car2.color = "blue"
# 动态添加属性
print(car1.__dict__)
print(car1.color)
print(car2.__dict__)
print(car2.color)

print(car1)


class Bus:
    def __init__(self, color: str, length: int, position: int = 0):
        self.color = color
        self.length = length
        self.position = position

    def move(self):
        self.position += 1
        print(f"向前走:{self.position}")


bus = Bus("red", 100)

print(bus.__dict__)
print(bus.color)
bus.color = "blue"
print(bus.color)
print(bus.length)
for i in range(5):
    bus.move()
