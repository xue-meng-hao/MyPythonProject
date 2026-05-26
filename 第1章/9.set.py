# 集合
set1 = {1, 2, 3}
set1.add(4)
print(set1)
print(type(set1))

set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set2)

set3 = set1.intersection(set2)
print(f"-------{set3}")
set3 = set1 & set2
print(set3)

set4 = set1.difference(set2)
print(set4)
set5 = set2.difference(set1)
print(set5)
set5 = set2 - set1
print(set5)

set6 = set1.union(set2)
print(set6)
set6 = set1 | set2
print(set6)

# 使用frozenset冻结集合，不能修改
set7 = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
for item in set7:
    print(item)
# set7[0]=10
print(set7)

# 集合可以嵌套不可变集合的原因：python底层会为其中的元素分配唯一的编号，编号是哈希值，内容变化哈希值也会变化，所以只有不可变的集合才能放到集合中

set8 = {1, 2, 4, set7}
print(set8)

# add向集合中添加元素
set8.add(10)
print(set8)
# update向集合中添加多个元素
set8.update({30, 40})
print(set8)

# remove删除集合中的元素,如果元素不存在会报错
set8.remove(30)
print(set8)
# set8.remove(30)
# print(set8)
# discard删除集合中的元素,如果元素不存在不会报错
set8.discard(40)
print(set8)

# pop随机删除集合中的元素，并返回该元素
a = set8.pop()
print(a)
print(set8)

# 集合常用方法：
# 集合A.difference(集合B):找到集合A中不同于集合B的元素，A和B都不变，返回一个新的集合

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
setC = setA.difference(setB)
print(setC)
setC = setB.difference(setA)
print(setC)

# 集合A.difference_update(集合B):从集合A中删除集合B中存在的元素（集合A被修改，集合B不变）,返回None
setB.difference_update(setA)
print(setA)
print(setB)

# 集合A.union(集合B):返回一个新的集合，包含集合A和集合B中的所有元素，集合A和集合B都不变
setD = setA.union(setB)
print(setD)

# 集合A.issubset(集合B):判断集合B是否为集合A的子集，返回值为boolean值
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
if setA.issubset(setB):
    print("setA是setB的子集")
else:
    print("setA不是setB的子集")

# 集合A.issuperset(集合B):判断集合A是否为集合B的父集，返回值为boolean值
if setB.issuperset(setA):
    print("setB是setA的父集")

# 集合A.isdisjoint(集合B):判断集合A和集合B是否没有交集，返回值为boolean值
if setA.isdisjoint(setB):
    print("setA和setB没有交集")
else:
    print("setA和setB有交集")

# 并集|，交集&，差集-，对称差集^
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
setC = setA | setB
print(setC)
setD = setA & setB
print(setD)
setE = setB - setA
print(setE)
# 对称差集，表示不存在setA但存在setB
setF = setA ^ setB
print(setF)
