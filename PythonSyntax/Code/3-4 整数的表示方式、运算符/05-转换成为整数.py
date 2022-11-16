# 使用int内置类可以将数据转换成为整数

a = '31'
b = int(a)
print(a)
print(b)
print((b + 1))

# x = 'hello'
# y = int(x)
# print(y)   报错
# 如果字符串不是合法数字，会直接报错

x = '1a2c'
y = int(x, 16)   # 把字符串当成十六进制转换为整数
print(y)  # 6700 打印一个数字，默认使用十进制输出
print(bin(y))

m = 'abc'
n = int(m, 16)
print(n)

m = '12'
n = int(m, 8)  # 把字符串的 12 当作八进制转换成整数
print(n)
