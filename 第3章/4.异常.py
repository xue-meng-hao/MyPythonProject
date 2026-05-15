# 使用try except捕获异常
while True:
    try:
        num = int(input())
        num = 1 / num
        print(num)
    # except ValueError as e:
    #     print(f"第一种异常:{e}")
    #     break
    # except ZeroDivisionError as e:
    #     print(f"第二种异常:{e}")
    #     break
    except Exception as e:
        print(e)

# 异常传递
# 调用的时候会层层上报
