# for i in range(10):
#     print(i)
# i = 0
# while i<10:
#     print(i)
#     i+=2
import token

# i = 1
# while i < 10:
#     print(i)
#     print("人生苦短，我用python")
#     i += 2
# else:
#     print("结束")

# i1=0
# sum1=0
# while i1<100:
#     if i1%2==0:
#         sum1=sum1+i1
#     i1+=1
# else:
#     print(sum1)
#
# total=0
# for i in range(1,100):
#     if i%2==0:
#         total=total+i
#         print(total,i)
# else:
#     print(total)

# s="this is test"
# for s1 in s:
#     print(s1)

# for i2 in range(100,200,3):
#     print(i2)
flag = False
for i3 in range(1, 100):
    for i4 in range(i3, 100):

        if i3 == 10:
            flag = True
            break
        else:
            print(f"i3:{i3},i4:{i4}")
    if flag:
        break

# for i in range(100):
#     print("*",end="")
