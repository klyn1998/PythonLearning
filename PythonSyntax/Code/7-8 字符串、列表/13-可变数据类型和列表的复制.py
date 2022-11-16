import copy
# python里的数据都是保存在内存里的
# 可变类型和不可变类型

# 不可变类型：字符串，数字，元祖
# 可变类型：列表，字典，集合

# 不可变数据类型，如果修改值，内存地址会发生变化
# 可变数据类型，如果修改值，内存地址不会发生变化

# 使用内置函数id，可以获取到一个变量的内存地址

a = 12
b = a
print('修改前，a=%X，b=%X' % (id(a), id(b)))  # a=7F811E121A90，b=7F811E121A90
a = 10
print(b)  # 12
print('a=%X，b=%X' % (id(a), id(b)))  # a=7F811E121A50，b=7F811E121A90

nums1 = [100, 200, 300]
nums2 = nums1
print('修改前nums1=%X，nums2=%X' % (id(nums1), id(nums2)))  # 修改前nums1=7FC0CFE7DA80，nums2=7FC0CFE7DA80

nums1[0] = 1
print(nums2)  # [1, 200, 300]
print('修改后nums1=%X，nums2=%X' % (id(nums1), id(nums2)))  # 修改后nums1=7FC0CFE7DA80，nums2=7FC0CFE7DA80
# x 和 y 指向同一个内存空间，会相互影响

# 调用copy方法，可以复制一个列表
# 这个列表和原有列表内容一样，但是指向不同的数据空间
x = [100, 200, 300]
y = x  # 等号是内存地址的赋值
z = x.copy()
x[0] = 1
print(y)
print(z)
print('0x%X, 0x%X, 0x%X' % (id(x), id(y), id(z)))

# 除了使用列表自带的 copy 方法以外，还可以使用copy模块实现拷贝
a = copy.copy(x)  # 效果等价于x.copy，都是一个浅拷贝
b = x.copy()
print(a, b)

# 深拷贝

# 切片其实就是一个浅拷贝
names1 = ['allen', 'bob', 'cindy', 'jack']
names2 = names1[::]
print(names1, names2)
names1[0] = 'jerry'
print(names1, names2)
