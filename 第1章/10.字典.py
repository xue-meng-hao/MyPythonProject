direct1 = {"张三": 1, 2: 2, 3: 3}
print(direct1)
print(direct1.get("张三"))
print(direct1.get(2))
print(direct1.get(3))
print(type(direct1))

direct1.update({"李四": 4})
print(direct1)

set1={1,23}
set2={"test","test"}
direct2={"set1":set1,"set2":set2}
print(direct2)

str1=direct2.get("test111","111")
print(str1)
print(direct2)
print(direct2["set1"])

for i in direct2.values():
    print("111"+str(i))

del direct2["set2"]
print(direct2)
pop1=direct2.pop("set1")
print(pop1)