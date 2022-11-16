# 使用bool内置类可以将其他数据类型转换成为布尔值
print(bool(100))  # 将数字100转换成为布尔值 True
print(bool(-1))  # -1转换成为布尔值 True
print(bool(0))  # 将 0 转换成为布尔值 False

# 数字里，只有数字 0 被转换成为布尔值False，其他数字转换成为布尔值都是True

print(bool('hello'))  # True
print(bool('False'))  # True
print(bool(''))  # False
# 字符串里，只有空字符串''可以转换成为False,其他字符串都转换成为True

# None转换成为布尔值是 False
print(bool(None))

print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False

# {} 空字典
# set() 空集合
# 数字0，空字符串''，空列表[]，空元组(),空字典{},空集合set(),空数据None会被转换成为False
# 其他都会被转换为True
# 计算机里，True和False其实就是使用数字1和0来保存的
print(True + 1)  # 2
print(False + 1)  # 1

# 隐式类型转换
if 3:  # True
    print('hello')
print(type(True))
