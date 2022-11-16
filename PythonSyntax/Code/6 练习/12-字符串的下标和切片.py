# 下标我们又称之为索引，表示第几个数据。

# 可迭代对象：str list tuple dict set range 都可以便利
# str list tuple 可以通过下标来获取或者操作数据

# 在计算机里，下标都是从0开始的。 0, 1, 2, 3, 4
word = 'excellent'  # 字符串：一个一个的字符串在一起 string
# 可以通过下标来获取或者修改指定位置的数据
print(word[4])  # l

# 字符串是不可变的数据类型。
# 对于字符串的任何操作，都不会改变原有的字符串！！！
# word[4] = 'x'  # 报错

# 切片就是从字符串里复制一段指定的内容，生成一个新的字符串
m = 'abcdefghijklmnopqrstuvwxyz'
print(m[5])  # m[index] ==> 获取指定下标上的数据

# 切片语法 m[start:end:step]
# step 指的是步长，可以理解为间隔。每隔step-1 个取一次
# step为负数，表示从右往左获取

print(m[2:9])  # 包含start，不包含end
print(m[2:])  # 如果只设置了start，会到最后
print(m[:9])  # 如果只设置了end,会从头开始

# 步长默认为1
print(m[3:15:2])  # dfhjln
print(m[3:15:1])   # defghijklmno
# print(m[3:15:0])  # 步长不能为0

# print(m[3:15:-1])  # 从右往左找，找不到，没有数据
print(m[15:3:-1])  # ponmlkjihgfe 还是包含start，不包含end
print(m[::])  # abcdefghijklmnopqrstuvwxyz 从头到尾复制
print(m[::-1])  # zyxwvutsrqponmlkjihgfedcba

# start和end如果是负数，表示从右边数
print(m[-9:-5])  # z是-1
print(m[-5:-9:-1])
