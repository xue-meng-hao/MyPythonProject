import re

s1 = "18833338888"
s2 = "我的手机号是15055557777，你知道吗？18833338888也是符合的吗？"

# match从开头开始匹配
result = re.match(r"1[3-9]\d{9}", s1)
print(result.group())
# 从字符串任意位置搜索，搜索到匹配的就不在搜索
result = re.search(r"1[3-9]\d{9}", s2)
print(result.group())
print(result.span())
print(result.start())
print(result.end())

# findall 搜索所有匹配的
result = re.findall(r"1[3-9]\d{9}", s2)
print(result)
print(*result)
