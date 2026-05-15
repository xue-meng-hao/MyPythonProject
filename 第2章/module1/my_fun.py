# __all__指定导入模块哪些功能
__all__ = ['out_line1']


def out_line():
    print("-" * 20)


def out_line1():
    print("-" * 30)


# 测试函数
__name__
print(__name__)
# 如果被当作模块导入，则下面的代码不执行
if __name__ == '__main__':
    out_line()
