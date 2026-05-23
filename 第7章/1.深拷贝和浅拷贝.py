# 赋值会导致修改一个影响另一个
import copy

# 浅拷贝,创建一个新的外部容器，但内部元素依然引用原来的对象
nums1 = [1, 2, 3]
nums2 = copy.copy(nums1)
print(nums1, nums2)
nums1[0] = 100
print(nums1, nums2)
# 浅拷贝嵌套数据仍然共享，修改嵌套数据会互相影响
nums1 = [[1, 2], [3, 4]]
nums2 = copy.copy(nums1)
print(nums1, nums2)
nums1[0][0] = 100
print(nums1, nums2)

# 深拷贝会创建一个新的外层容器，并将内部所有可变对象进行递归复制
nums1 = [[1, 2], [3, 4]]
nums2 = copy.deepcopy(nums1)
print(nums1, nums2)
nums1[0][0] = 100
print(nums1, nums2)
# 深拷贝可以彻底消除数据修改的影响；深拷贝遇到不可变对象不会复制，会直接引用

# 深拷贝注意点：
# 1. 深拷贝只复制可变对象，不可变对象会直接引用
# 2. 元组中如果只包含不可变对象，则深拷贝不起作用，如tuple就是不起作用的
