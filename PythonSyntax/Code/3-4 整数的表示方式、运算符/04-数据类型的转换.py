# 进制转换  将int 类型以不同的进制表现出来
# 类型转换  将一个类型的数据转换为其他类型的数据
# int ==> str   str ==> int  bool ==> int
age = input('输入年龄')

# print(age+1) 错误
# 原因：input 接收到的用户输入，都是str字符串类型
# 在Python里，如果字符串和数字做加法运算，会直接报错
# 把字符串类型的变量 age 转换为数字类型的 age

# 使用 int 内置类可以将其他类型数据转换成为整数
new_age = int(age)
print(new_age + 1)

# 为什么转换数据类型：不同的数据类型进行运算时，运算规则不同。
