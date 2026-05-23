# 1. 局部作用域:Local
# 2. 外层函数作用域:Enclosing
# 3.全局作用域: Global
# 4. 内建作用域:Built-in
# LEGB = Local -> Enclosing -> Global -> Built-in

a = 10


def outer():
    b = 20
    c = 10

    def inner():
        # 声明变量a为全局变量
        global a
        a = 30
        # 声明变量c为外层函数变量
        nonlocal c
        c = 30
        print(a, b, c)

    inner()
    print(c)


print(a)

outer()
