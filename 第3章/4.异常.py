# 使用try except捕获异常
# while True:
#     try:
#         num = int(input())
#         num = 1 / num
#         print(num)
#     # except ValueError as e:
#     #     print(f"第一种异常:{e}")
#     #     break
#     # except ZeroDivisionError as e:
#     #     print(f"第二种异常:{e}")
#     #     break
#     except Exception as e:
#         print(e)

# 异常传递
# 调用的时候会层层上报

# 通过traceback模块查看异常信息

try:
    num = int(input())
    num = 1 / num
    print(num)
except (ZeroDivisionError, ValueError) as e:
    print(f"错误行号:{e.__traceback__.tb_lineno}")
else:
    print("没有异常")
finally:
    print("无论是否有异常都会执行")
