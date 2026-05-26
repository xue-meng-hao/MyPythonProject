import os

# 创建单级文件夹
# os.mkdir("test")
# # 创建多级文件夹
# os.makedirs("test/test1/test2")
# # 删除单级文件夹
# os.rmdir("test")
# # 删除多级文件夹
# os.removedirs("test/test1/test2")
# # 判断文件夹是否存在
# os.path.exists("test")
# isdir判断是否为目录
# isfile判断是否为文件
# scandir扫描指定目录
# for i in os.scandir("."):
#     print(i.name, i.is_dir(), i.is_file())

# walk按层级，遍历指定目录，所有子目录下的目录和文件
# for root, dirs, files in os.walk("."):
#     print(root, dirs, files)

# 删除有内容的目录：
import shutil
#删除test目录下所有的文件
shutil.rmtree("test")
