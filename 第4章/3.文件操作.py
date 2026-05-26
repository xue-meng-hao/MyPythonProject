# f=open("1.txt","r",encoding="utf-8")
# print(f.read())
# f.close()
import os.path

try:
    with open("test.py", "r", encoding="utf-8") as f1:
        for line in f1:
            print(line, end="", flush=True)
except FileNotFoundError:
    print("文件不存在")
except Exception as e:
    print(e)

# 使用w进行写操作
try:
    with open("静夜思.txt", "w", encoding="utf-8") as f1:
        f1.write("窗前明月光，\n")
        f1.write("疑是地上霜。\n")
        f1.write("举头望明月，\n")
        f1.write("低头思故乡。")
except Exception as e:
    print(e)
# 使用r进行写操作

try:
    with open("静夜思.txt", "r", encoding="utf-8") as f1:
        print(*f1.read())
except Exception as e:
    print(e)
# 使用a类型向文件进行追加
with open("静夜思.txt", "a", encoding="utf-8") as f1:
    f1.write("\n这是追加的")

# if os.path.exists("test"):
#     os.remove("test")
# else:
# os.mkdir("test")
dirlist = os.listdir("C:/Users/Administrator/PycharmProjects/MyPythonProject/第4章")
my_dir_list = []
for name in dirlist:
    if name.endswith(".py"):
        my_dir_list.append(name[:-5])
print(my_dir_list)

# 三元运算符
a = "1" if not my_dir_list[0] else "2"
print(a)



import os

if not os.path.isdir("./json"):
    os.makedirs("./json")
# with open("./json.json", 'rb') as f1, open("./json/json.json", "wb") as f2:
#     data = f1.read()
#     f2.write(data)

# 处理大文件时候，不一次性读出所有数据再写入，而是将数据分批读取，写入
with open("./json.json", 'rb') as f1, open("./json/json.json", "wb") as f2:
    while True:
        data = f1.read(1)
        print(data)
        if len(data) == 0:
            break
        f2.write(data)
    print("copy over")
