# 大于>  小于<  大于等于>=  小于等于 <= 不等于!=/<> 等等于==
print(2 > 1)  # True
print(2 < 4)  # True
print(4 >= 3)  # True
print(5 != 6)  # True
print('hello' == 'hello')  # True
a = 5
b = 5
print(a == b)

# 比较运算符在字符串里的使用
# 字符串之间使用比较运算符，会根据各个字符的编码值逐一进行比较
# ASCII码表 a-z A-Z
print('a' > 'b')  # False  97<98
print('abc' > 'b')  # False  97 98 99逐一进行比较

# 数字和字符串之间，做==运算的结果是False,做!=结果是True，不支持其他的比较运算。
# print('a' > 90)  报错
print('a' == 90)
print('a' != 97)
