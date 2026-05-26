# 函数中包含yield关键字，函数就是生成器函数

# 写在生成器中的代码，需要通过生成器对象来执行
# 调用__next__方法会让生成器函数代码开始执行，生成器中代码开始执行后，遇到yield会暂停执行，并内部记录暂停位置，后续继续调用__next__方法，会从暂停位置继续执行，直到遇到下一个yield，再次暂停，以此类推
# 遇到return会触发StopIteration异常，并返回return后面的值作为异常信息
# yield关键字后面写的表达式，会作为本次__next__方法的返回值

# region
# def test():
#     print("1")
#     yield 2
#     print("3")
#     yield 4
#     # 遇到return会抛出StopIteration异常
#     return 5
#
#
# g = test()
# print(type(g))
# print(g.__iter__())
# print(g.__next__())
# newG = iter(g)
# print(newG)
# next(g)
# next(g)
# try:
#     next(g)
# except StopIteration as e:
#     print(e.value)
# print(next(g))
# print(next(g))
# print(next(g))
# endregion

# 生成器就是一种特殊迭代器

# region
# # yield from能把一个[可迭代对象]里的东西依次yield出来，代替：for+yield
# def demo():
#     nums = [1, 2, 3, 4, 5]
#     yield from nums
#     #等价于
#     # for i in nums:
#     #     yield i
#
# # d=demo()
# # r1=next(d)
# # print(r1)
#
# for item in demo():
#     print(item)
# endregion

# 可以使用send方法，继续执行生成器yield暂停的部分，并传递参数
# 第一次使用生成器不能使用send，只能使用next，因为生成器内部没有记录上一次暂停的位置，使用send(None)可以，因为和next一样
# def test():
#     print("1")
#     a = yield 2
#     print(a)
#     b = yield 3
#     print(b)
#
#
# t = test()
# next(t)
# # next(t)
# t.send(100)
# try:
#     t.send(200)
# except StopIteration as e:
#     print(e)
# # next(t)

# region
# 用生成器实现类中属性迭代
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__attrs=[name, age]

    def __iter__(self):
        yield from [self.name, self.age]


p = Person("张三", 18)
for item in p:
    print(item)
# endregion


# region
# # 用生成器写斐波那契
# def fibonacci(total):
#     prev = 1
#     curr = 1
#     for index in range(total):
#         if index < 2:
#             yield 1
#         else:
#             temp = curr
#             curr = prev + curr
#             prev = temp
#             yield curr
#
#
# fib = fibonacci(10)
# print(fib)
# # 无论是迭代器还是生成器都可以使用容器对象如list,tuple,set,dict等接收所有的内容，因为他们都是可迭代对象
# print(list(fib))
# endregion

# 生成器表达式：一种类似列表推导式的语法，快速创建生成器对象的方式
# 语法格式：(表达式 for循环变量 in可迭代对象)，和列表推导式一样，只是生成器表达式是用()代替[]
list1 = [n * 2 for n in range(10)]
print(list1)

g = (n * 2 for n in range(10))
print(list(g))

# 当每一个结果只依赖当前结果，可以使用生成器表达式
