a = b = c = d = 'hello'
print(a, b, c, d)

# x = 'yes' = y = z 错误

m, n = 3, 5  # 拆包
print(m, n)

x = 'hello', 'good', 'yes'
print(x)  # ('hello', 'good', 'yes')  元组

# 拆包时，变量的个数和值的个数不一致，会报错
# y, z = 1, 2, 3, 4, 5 错误
# o, p, q = 4, 2  错误

# *表示可变长度
o, *p, q = 1, 2, 3, 4, 5, 6
print(o, p, q)  # 1 [2, 3, 4, 5] 6

*o, p, q = 1, 2, 3, 4, 5, 6
print(o, p, q)  # [1, 2, 3, 4] 5 6
