# 编写hello world
# python注释，python解释器会忽视注释
# print("hello world")
# print("hello python")
#
#
# print(False-1)
#
# print(True-1)
#
num = 1.3455
print(num)

num += 1
print(num)

num = "OK"
print(num)

base, incr = 1, 2
print(base + incr)
test1, test2, test3 = 1, 3, 5
print(test1 + test2 - test3)

a = 100
b = 200
c = 300

d = c
c = b
b = a
a = d
print("a=" + str(a), "b=" + str(b), "c=" + str(c))

print(type("test" + str(a)))

print(type(a))

print(type(None))

print(isinstance(True, bool))

print(isinstance(3, bool))

s = """
 三引号的定义方式
 这是一个测试
 
 这是一个测试空行的测试
 
 这是一个测试
"""
print(s)
print(type(s))

s1 = "this is \" a \" name"
print(s1)
print(type(s1))

s2 = "this is 换行符 \n\" a \" name"
print(s2)
print(type(s2))

s3 = "大家好，我是%s,我喜欢%s"
s31 = "测试"
s32 = "test"
print(s3 % ("test111", s32))

print(s3 % ("测试", "占位符"))

s4="这是一个测试"
s5=f"这是一个测试s4:{s4}的字符串"
print(s5)
