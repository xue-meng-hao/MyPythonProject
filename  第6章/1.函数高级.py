def welcome(str):
    print(f"Welcome!{str}")


# 函数也是一个对象
print(type(welcome))
# 函数可以动态添加属性
welcome.desc = "This is a welcome function"
print(welcome.desc)
# 函数可以赋值给变量

say_hello = welcome
say_hello("hello")
print(say_hello.desc)

a = 666


def test(t1):
    print(id(t1))
    t1 = 999
    print(id(t1))


test(a)
# 可变对象
list1 = [1, 2, 3]
print(id(list1))
list1[0] = 33
print(id(list1))


# 函数也可以作为参数

def test2(t1):
    print(f"调用了test2:{id(t1)}")
    t1("test2测试test1")


test2(welcome)


# 函数也可以作为返回值
def test3(t1):
    t1.desc = "哈哈哈"
    return t1


ret = test3(welcome)
print(ret.desc)
ret("测试")
