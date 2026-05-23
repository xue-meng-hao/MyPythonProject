def show(*args, **kwargs):
    print(args, kwargs)


# 将"a", "b", 8打包到args中，将name="zhangsan", age=20打包到kwargs中
show("a", "b", 8, name="zhangsan", age=20)

nums = (10, 20, 30)
person = {"name": "zhangsan", "age": 20}
# 解包传递参数
show(*nums, **person)
