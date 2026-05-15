name: str = "姓名"
age: int = 10
gender: int | str = "male"
print(name)
print(age)
print(type(gender))

# 使用name:str做类型注解

names = ["a1", "b1", "c1", 11]
print(names)


def cclt(name1: str, age1: int) -> tuple[str, int]:
    print(name1)
    print(age1)
    return name1, age1


t1=cclt("name, age", 1)
print(t1)