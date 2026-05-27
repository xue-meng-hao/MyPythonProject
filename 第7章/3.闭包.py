# def outer():
#     a = 10
#
#     def inner():
#         nonlocal a
#         a += 1
#         print(hex(id(a)))
#         print(a)
#
#     return inner
#
#
# f = outer()
# f()
# print(f.__closure__)

# outer函数中被inner使用的变量，会被封存到闭包单元cell中，形成一个闭包
# 这些cell会组成一个__closure__属性，它是一个元组，每个元素都是一个cell对象


# 闭包产生的条件：
# 1、嵌套函数
# 2、内层函数引用了外层函数的变量
# 3、外层函数返回了内层函数


# 闭包注意点：
# 1. 调用n次外部函数，就会得到n个不同的闭包，并且闭包直接互不影响
# 2. 内层函数中用到的外部变量是可变对象，多个闭包之间依然互不影响

def outer():
    a = []

    def inner(value):
        a.append(value)
        print(a)

    return inner


f = outer()
f(4)
f(5)
f(6)
print(f.__closure__)

f1 = outer()
f1(7)
f1(8)
print(f1.__closure__)


# 闭包优点：
# 1. 可以记住状态：不用全局变量也不用写类，就能在多次调用之间保存数据
# 2. 可以做“配置过的函数”：先传一部分参数，把环境固定，得到一个定制版的函数
# 3. 可以实现简单的“数据隐藏”：外层变量对外不可见，只能通过闭包函数来访问
# 4. 可以实现“装饰器”功能

def beauty(char, n):
    def show_msg(message):
        print(char * n + message + char * n)

    return show_msg


show = beauty('*', 3)
show('你好')

# 缺点：
# 1. 理解成本高
# 2. 如果引用很大的对象，又长期不释放，会增加内存占用
# 3. 很多场景下，用（类+实例属性）会更清晰，闭包不一定是最优解
