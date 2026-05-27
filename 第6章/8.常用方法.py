import time

# print函数
# for index in range(1,101):
#     print(f"\r已加载{index}%",end='',flush=True)
#     time.sleep(0.1)

# round函数
# 使用的是银行家舍入法：小于5就舍，大于5就进，等于5时，如果后面的数字是偶数就舍，奇数就进
print(round(2.5))
print(round(3.5))
print(round(2.4))
print(round(3.6))

# zip函数，将多个序列一一配对
names = ['张三', '李四', '王五']
ages = [18, 20, 22]
for name, age in zip(names, ages):
    print(name, age)

dirc1 = {name: age for name, age in zip(names, ages)}
print(dirc1)
