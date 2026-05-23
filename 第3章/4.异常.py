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

# try:
#     num = int(input())
#     num = 1 / num
#     print(num)
# except (ZeroDivisionError, ValueError) as e:
#     print(f"错误行号:{e.__traceback__.tb_lineno}")
# else:
#     print("没有异常")
# finally:
#     print("无论是否有异常都会执行")

# 手动抛出异常使用raise
# try:
#     age = int(input())
#     if age < 0 or age > 120:
#         raise ValueError("年龄错误")
# except ValueError as e:
#     print(e)

# 自定义异常类
# class AgeException(Exception):
#     pass


# try:
#     age = int(input())
#     if age < 0 or age > 120:
#         raise AgeException("年龄错误")
# except AgeException as e:
#     print(e)


# 自定义异常类
class SchoolNameException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__("异常信息:" + self.msg)


try:
    schoolName = str(input())
    if len(schoolName) > 10 or "学校" not in schoolName:
        raise SchoolNameException("校名错误")
except SchoolNameException as e:
    print(e)
else:
    print("校名正确")
