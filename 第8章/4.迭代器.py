# region
"""
使用__iter__方法确定是否为可迭代对象
"""
# endregion

string = 'hello'
print(string.__iter__())
# 1. __iter__方法是一个魔法方法，当调用iter函数时候，__iter__方法会被调用
# 2. 可迭代对象.__iter__等于iter(可迭代对象)
# 3. 使用iter(可迭代对象)返回一个迭代器(iterator)，则对象就是可迭代对象
print(iter(string))


#创建自定义迭代器，需要实现__iter__方法和__next__方法
