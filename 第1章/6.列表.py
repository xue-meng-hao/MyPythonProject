mylist = ["123", 123, True, 'hello']
# print(list)
# # list[0]=1
# for i in list:
#     print(type(i))
#     print(i)
#
# list.__len__()
# print(mylist.__len__())
# print(len(mylist))
# for i in range(len(mylist)):
#     print(-i-1)
#     print(mylist[-i-1])

# print(mylist[1:3])
#
# print(mylist[1:4:2])
#
# mylist.append("10086")
# mylist.insert(0,"000")
# print(mylist)
# mylist.remove(123)
# print(mylist)
# mylist.pop()
# print(mylist)
#
#
# mylist = [123,111,333,222]
# mylist.sort()
# print(mylist)
# mylist.reverse()
# print(mylist)


# num_list=[]
# for i in range(10):
#     num=int(input("请输入："))
#     num_list.append(num)
#     print(num_list)
# num_list.sort(reverse=True)
# num_list.reverse()
# print(num_list)
# print("平均值：",sum(num_list)/len(num_list))
# print(1 in num_list)

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [333, 444, 555, 666]
# 解包和组包
num_list3 = [*num_list1, *num_list2]
print(num_list3)
num_list1.append(666)
print(num_list1)
num_list4 = num_list1 + num_list2
print(num_list4)

# 列表推导式
num_list5 = [i ** 2 for i in range(1, 21)]
print(num_list5)

num_list6 = [i ** 2 for i in range(1, 21) if i % 2 == 0]
print(num_list6)

list11 = [1, 2, 3, 4, 5]
# 使用append添加
list11.append(6)
print(list11)

list12 = [1, 2, 3, 4, 5]
# 使用insert添加
list12.insert(0, 6)
print(list12)

list13 = [1, 2, 3, 4, 5]
# 使用extend添加
list13.extend("test")
print(list13)

list14 = [1, 2, 3, 4, 5]
# 使用pop删除指定下标的数
value = list14.pop(0)
print(value)
print(list14)

list15 = [1, 2, 3, 4, 5]
# 使用remove删除列表中第一个出现的值
list15.remove(3)
print(list15)

list16 = [1, 2, 3, 4, 5]
# 使用clear清空列表
list16.clear()
print(list16)

list17 = [1, 2, 3, 4, 5]
# 使用del删除指定下标值
del list17[0]
print(list17)

# 使用enumerate遍历列表，通过enumerate可以同时获取下标和元素
for index, item in enumerate([1, 2, 3]):
    print(index, item)
