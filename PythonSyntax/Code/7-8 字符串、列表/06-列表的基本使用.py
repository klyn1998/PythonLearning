# 当我们有多个数据需要按照一定顺序保存时，可以考虑列表
# name1 = '张三'
# name2 = '李四'
# name3 = 'jack'

# 使用 [] 来表示一个列表，列表里的每一个数据称为元素
# 元素之间使用逗号进行分隔
names = ['jack', 'allen', 'alice', 'bob', 'cindy', 'chuck']

# 和字符串一样，都可以使用下标来获取元素和对元素进行切片
# 同时，还可以使用下标来修改列表里的元素
print(names[3])
names[3] = 'saul'
print(names)

# 也可以通过下标来切片
print(names[1:4])

# x = 'hello'
# print(x[1])
# x[0] = 'm'  # 字符串只能获取，不能修改，字符串是不可变数据类型

# 可以使用list 将可迭代对象转换为一个列表
# names = list(('jack', 'allen', 'alice', 'bob', 'cindy', 'chuck'))
# print(names)
