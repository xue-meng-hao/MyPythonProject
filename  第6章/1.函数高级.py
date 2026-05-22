def welcome():
    print("Welcome!")


# 函数也是一个对象
print(type(welcome))
# 函数可以动态添加属性
welcome.desc = "This is a welcome function"
print(welcome.desc)
# 函数可以赋值给变量

say_hello = welcome
say_hello()
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
