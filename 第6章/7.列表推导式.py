# 列表推导式：用一条语句从可迭代对象中生成新列表的语法结构，语法格式：[表达式 for 变量 in 可迭代对象]，可以使用append代替

list1 = [i * i for i in range(10)]
print(list1)

# 待条件：[表达式 for 变量 in 可迭代对象 if 条件]
list2 = [i * i for i in range(10) if i % 2 == 0]
print(list2)

# 字典推导式：{key:value for key,value in zip(可迭代对象1,可迭代对象2)}
names = ['zhangsan', 'lisi', 'wangwu']
ages = [10, 20, 30]
dict1 = dict(zip(names, ages))
print(dict1)
dict2 = {name: age for name, age in zip(names, ages)}
print(dict2)
dict3 = {names[index]: ages[index] for index in range(len(names))}
print(dict3)

# 集合推导式：{表达式 for 变量 in 可迭代对象}
result = {name for name in names}
print(result)

# 生成器推导式：(表达式 for 变量 in 可迭代对象)
gen = (i * i for i in range(10))
for item in gen:
    print(item)
# python中没有元组推导式


