# 装饰器是一种可调用对象（通常是函数），能接收一个函数作为参数，并返回一个新函数
# 装饰器可以在不修改原函数的前提下，增强或改变原函数的功能

# def decorator(func):
#     def wrapper():
#         func()
#         print("wrapper of decorator")
#
#     return wrapper
#
#
# @decorator
# def greet():
#     print("hello world")


# greet()

# @decorator相当于greet=decorator(greet)
# 带参数的装饰器，三层嵌套：
# 第一层：接收配置
# 第二层：接受函数
# 第三层：接受参数


def add_pro(msg):
    def outer(func):
        def wrapper(*args, **kwargs):
            """
            装饰器包装函数，在被装饰函数执行前后添加额外的打印功能。

            Args:
                *args: 传递给被装饰函数的位置参数
                **kwargs: 传递给被装饰函数的关键字参数

            Returns:
                被装饰函数的执行结果
            """
            print(f"before call,msg={msg}")
            res = func(*args, *kwargs)
            print(f"after call,msg={msg}")
            return res

        return wrapper

    return outer


@add_pro("my test message")
def add(x, y):
    res = x + y
    print(f"{x}+{y}的结果是：{res}")
    return res


add(1, 2)


# 装饰器的应用场景
# 1. 日志2. 性能监控3. 安全检查4. 缓存5. 事务6. 单例7. 回滚8. 版本控制9. 权限检查

# 多个装饰器一起使用,顺序是先外层的装饰器，再到内层的装饰器

def test1(func):
    def wrapper(*args, **kwargs):  # 定义装饰器函数
        print("before test1")
        res = func(*args, **kwargs)
        print("after test1")
        return res

    return wrapper


def test2(func):
    def wrapper(*args, **kwargs):  # 定义装饰器函数
        print("before test2")
        res = func(*args, **kwargs)
        print("after test2")
        return res

    return wrapper


@test1
@test2
def test(x, y):
    print(f"{x},{y}")
    return x, y


test(1, 2)


# 类装饰器
# 1. 包含__call__方法的类，就是类装饰器
# 2. 像调用函数一样调用类装饰器的实例对象，就会触发__call__方法
# 3. __call__方法通常接收一个函数作为参数，并返回一个新函数


# 手动装饰
# def add(x, y):
#     res = x + y;
#     print(f"{x}+{y}的结果是：{res}")
#     return res
#
#
# class SayHello:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('hello')
#             res = func(*args, **kwargs)
#             print('goodbye')
#             return res
#
#         return wrapper
#
#
# say_hello = SayHello()
# # say_hello.__call__(add)(1, 2)
# say_hello(add)(1, 2)

# 自动装饰


class SayHello:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'hello,{self.msg}')
            res = func(*args, **kwargs)
            print('goodbye')
            return res

        return wrapper


# 类装饰器必须要写括号，否则会报错
@SayHello("test message")
def add(x, y):
    res = x + y;
    print(f"{x}+{y}的结果是：{res}")
    return res


# 类装饰器传参数,在__init__方法传递参数


# say_hello = SayHello()
# # say_hello.__call__(add)(1, 2)
# say_hello(add)(1, 2)


add(1, 2)
