# map函数,对一组数据中的每个元素，统一执行某种操作,并省成一组新数据
nums = [1, 2, 3]
new_nums = []
for num in nums:
    new_nums.append(num * 2)
print(new_nums)

new_nums = list(map(lambda num: num * 2, nums))
print(new_nums)
# map函数的返回值是一个迭代器对象，需要手动遍历，或手动类型转换
new_nums = list(map(lambda num: num ** 2, nums))
print(new_nums)
print(nums)

new_tuple = tuple(map(lambda num: num ** 2, nums))
print(new_tuple)

strs = {'3', '2', '1'}
list1 = list(map(int, strs))
print(list1)
list1 = tuple(map(int, strs))
print(list1)

list1 = set(map(int, strs))
print(list1)

# map函数注意点：
# 1. map只有在需要结果的时候才计算
# 2.返回的是迭代器对象，一旦遍历完成，就会被耗尽
# 3.map不改变元素数量

# filter函数,对一组数据中的每个元素，判断是否满足某种条件，如果满足，则留下，否则舍弃，格式：filter(函数，可迭代对象)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_odd(num):
    return num % 2 == 1


new_nums = filter(is_odd, nums)
print(list(new_nums))

print(list(filter(lambda num: num % 2 == 0, nums)))

# 筛选成年人
persons = [{'name': '张三', 'age': 18}, {'name': '李四', 'age': 20}, {'name': '王五', 'age': 16}]
adult_persons = list(filter(lambda person: person['age'] >= 18, persons))
print(adult_persons)

# 筛选非空字符串
strs = ['a', '', 'b', None, 'c', ' ', 'd']
not_empty_strs = list(filter(lambda n: n, strs))
print(not_empty_strs)
# filter注意点：
# 1. 延迟执行：不会立即筛选，只有在"需要结果时"才会进行筛选
# 2. 返回的是迭代器对象，一旦遍历完成，就会被耗尽
# 3. 不会改变元素数量

# filter不传递函数，会默认过滤"False"值

# sorted函数,对一组数据进行排序，默认升序排列，格式：sorted(可迭代对象，key=函数, reverse=False)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_nums = sorted(nums)
print(new_nums)

new_nums = sorted(nums, reverse=True)
print(new_nums)

new_nums = sorted(nums, key=lambda num: -num)
print(new_nums)

# 按照字符串长度排序
strs = ['abc', 'abcd', 'ab', 'a', 'abcde']
new_strs = sorted(strs, key=len)
print(new_strs)

# reduce函数,对一组数据不断合并，最终归并成一个结果，格式：reduce(合并函数，可迭代对象，初始值)
# 从functools模块导入reduce函数
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda a, b: a + b, nums)
print(sum)
