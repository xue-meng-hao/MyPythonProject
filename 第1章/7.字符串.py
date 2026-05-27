s = "12345678"
# print(s[1])
# print(s[:2])
# print(s[1:89:1])
i = s.find("3456789")
print(i)
print(s.split("3"))
s += "11 "
print(s.strip("3"))

# strip方法会从字符串两端开始删除，知道遇到第一个不在指定字符串中的字符就停下
s = "this is a test"
s1 = s.strip("th")
print(s1)
# strip不传参数，默认删除空格
s = " this is a test "
s1 = s.strip()
print(s1)
# lstrip方法只删除左边，rstrip只删除右边
s = " asrfa "
s1 = s.lstrip()
print(s1)

s = "this is a test"
s1 = s.rstrip("th")
print(s1)
