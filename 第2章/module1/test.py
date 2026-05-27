name = "name"
age = 10
__all__ = [name]

print(__name__)

if __name__ == '__main__':
    print("我是module1.test")
else:
    print("我不是主程序")
