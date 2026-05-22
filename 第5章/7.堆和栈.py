a=666
b=a
print(a)
print(b)
print(id(a))
print(id(b))
a=888
print(a)
print(id(a))
print(id(b))

a=[1,2,3]
print(id(a))
print(id(a[0]))