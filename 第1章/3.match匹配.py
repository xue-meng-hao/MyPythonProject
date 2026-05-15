num = input("输入数字")
a = ""
match int(num):

    case 1:
        a = "1"
    case 2:
        a = "t"
    case num if(num%3!=0):
        a = "e"
    case _:
        a = "a"

print(a)
