# 魔法方法
# __init__初始化方法
# __str__字符串表示的方法
# __eq__比较两个对象是否相等
# __lt__,__le__,__gt__,__ge__比较两个对象大小，lt小于，le小于等于，gt大于，ge大于等于

class Bus:
    def __init__(self, color: str, length: int):
        self.color = color
        self.length = length
        print("-" * 3)

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __eq__(self, other):
        return self.length == other.length


bus1 = Bus("blue", 3)
bus2 = Bus("red", 2)

print(bus1 < bus2)

print(bus1 >= bus2)
