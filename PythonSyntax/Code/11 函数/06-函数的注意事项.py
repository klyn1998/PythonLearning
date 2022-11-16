# 函数的三要素：函数名、参数、返回值
# 在有一些编程语言里，允许函数重名，在Python里不允许函数重名
# 如果函数重名，后一个函数会覆盖前一个函数

# def test(a, b):
#     print('a = {}, b = {}'.format(a, b))

# test = 对应的是一个函数
def test(x):
    print('good, x = {}'.format(x))


# test = 5
test(2)

# Python里，函数名也可以理解成为一个变量名，函数会被变量覆盖

# input = 2
# input('请输入密码')  # 报错

int = 5
print(int)
# int('45')


