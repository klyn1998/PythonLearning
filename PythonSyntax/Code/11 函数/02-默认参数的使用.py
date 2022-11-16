# def say_hello(city='Tokyo', name, age):  # 缺省参数要放在位置参数后面

def say_hello(name, age, city='Tokyo'):  # 形参city设置了一个默认值
    print('大家好，我是{}，今年{}岁了，来自{}'.format(name, age, city))


say_hello('allen', 18)  # 如果没有传递参数，会使用默认值
say_hello('tony', 20, 'Beijing')  # 如果传递了，就使用传递的实参
say_hello(name='tony', age=23, city='Nanjing')

# 如果有位置参数和关键字参数，关键字参数一定要放在位置参数的后面
say_hello('bob', 27, city='Osaka')  # 可以直接传递单个参数，也可以使用变量赋值的形式传输

# 缺省参数：
# 如果你传递了参数，就使用传递的参数
# 如果没有传递，就使用默认的值

# print函数里end就是一个缺省参数
print('hello world', '你好', sep='____')
print('hi')
