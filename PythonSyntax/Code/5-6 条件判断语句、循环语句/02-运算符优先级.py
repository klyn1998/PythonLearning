print(10 - 2 * 3)  # 4
print(10 + 2 * 3 ** 2)  # 28

# 逻辑运算的优先级：not > and > or
print(True or False and True)
print(False or not False)
print(True or True and False)

# 在开发中，使用括号说明运算符的优先级
print(True or (True and False))

# 逻辑运算符规则：
# 逻辑与运算：有一个是False，就是False；只有所有的运算数都是True，结果才是True
# 短路：只要遇到了False，就停止，不再继续执行
# 取值：取第一个为False的值，如果所有的运算数都是True，取最后一个运算数

# 逻辑或运算规则：
# 只要有一个运算数是True，结果就是True；只有所有的运算数都是False，结果才是False
# 短路：只要遇到了True，就停止，不再继续执行
# 取值：取第一个为True的值，如果所有的运算数都是False，取最后一个运算数
