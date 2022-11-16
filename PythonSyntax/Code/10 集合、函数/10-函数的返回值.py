# 返回值就是函数执行的结果，并不是所有的函数都必须要有返回值
def add(a, b):
    c = a + b  # 变量c在外部不可见，只能在函数内部使用
    return c  # return 表示一个函数的执行结果


result = add(1, 2)
print(result ** 4)

# 如果一个函数没有返回值，他的返回就是None
# print就是一个内置函数
x = print('hello')  # Function 'print' doesn't return anything
print(x)  # None

y = int(input('请输入你的年龄'))
print(y)
