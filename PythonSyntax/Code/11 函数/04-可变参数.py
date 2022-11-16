# *args 表示可变位置参数
# **kwargs 表示可变的关键字参数
# 缺省参数放在*args后面
def add(a, b, *args, mul=1, **kwargs):
    print('a = {}, b = {}'.format(a, b))
    print('args = {}'.format(args))  # args = (7, 8) 多出来的位置参数会以元祖的形式保存到args里
    print(kwargs)  # {'x': 0, 'y': 4} 多出来的关键字参数会以字典形式保存
    c = a + b
    for arg in args:
        c += arg
    return c * mul


print(add(1, 3, 7, 8, mul=2, x=0, y=4))
