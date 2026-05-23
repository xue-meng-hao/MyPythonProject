set1={1,2,3}
set1.add(4)
print(set1)
print(type(set1))

set2={1,2,3,4,5,6,7,8,9,10}
print(set2)

set3=set1.intersection(set2)
print(set3)
set3=set1&set2
print(set3)

set4=set1.difference(set2)
print(set4)
set5=set2.difference(set1)
print(set5)
set5=set2-set1
print(set5)

set6=set1.union(set2)
print(set6)
set6=set1|set2
print(set6)


