# Python里的for循环指的是for...in循环
# for 语句格式：
# for ele in iterable

# range 内置类用来生成指定区间的整数序列
# 注意：in的后面必须是一个可迭代对象！！！
# 目前接触的可迭代对象：字符串、列表、字典、元组、集合、range

# range 便利操作，一个一个拿出来
for i in range(1, 11):  # 包含左边，不包含右边
    print(i)

for y in 'hello':
    print(y)

# for m in 10:  # 错误 in的后面必须是一个可迭代对象
#     print(m)

z = 0  # 定义一个变量，用来保存所有数字之和
for a in range(1, 101):
    z += a
print(z)
