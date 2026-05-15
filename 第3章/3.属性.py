# 实例属性
# 类属性
# 类属性定义在类中
class Bus:
    length: int = 0

    def __init__(self, color: str, length: int):
        self.color = color
        self.length = length

    def __str__(self):
        return f"颜色:{self.color},长度:{self.length}"


bus1 = Bus("blue", 1)
bus2 = Bus("red", 2)
print(Bus.length)
print(bus2.length)

print(type(bus1))
