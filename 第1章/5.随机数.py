import random

random_number = random.randint(1, 100)
while True:
    a = int(input("请输入："))
    if a == random_number:
        print(f"输入正确，数字{random_number}")
        break
    else:
        print("输入错误")
        if (a < random_number):
            print("太小了")
        else:
            print("太大了")
