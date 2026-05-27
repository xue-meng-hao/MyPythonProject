# 没有名字的表达式，使用lambda关键字定义匿名函数，格式为: lambda 参数列表: 表达式
print((lambda x: x ** 2)(-10))

add = lambda x, y: x + y
print(add(1, 2))
#注意点：
# 1. 匿名函数只能写一行，不能写多行
# 2. 不能写代码块
# 3. 冒号右边必须是表达式，且只能写一个表达式
# 4. 表达式结果自动作为返回值
print((lambda x, y: x + y)(11, 2))
