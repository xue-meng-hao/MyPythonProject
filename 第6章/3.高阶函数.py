# 高阶函数：一个函数的参数是函数或者返回值是函数，则该函数为高阶函数
def add_num(a, f):
    return f(a)


print(add_num(-10, abs))
