# 装饰器是一种可调用对象（通常是函数），能接收一个函数作为参数，并返回一个新函数
# 装饰器可以在不修改原函数的前提下，增强或改变原函数的功能

def decorator(func):
    def wrapper():
        func()
        print("wrapper of decorator")

    return wrapper


@decorator
def greet():
    print("hello world")


greet()
