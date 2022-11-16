# {} 也可以进行占位
# format不用考虑数据类型

# {} 什么都不写，会读取后面的内容，一一对应填充
x = '大家好，我是{}，我今年{}岁了'.format('张三', 18)
print(x)

# {number} 根据数字的顺序来进行输入。数字从0开始
y = '大家好，我是{1}，我今年{0}岁了.'.format(20, 'jerry')

# {变量名}
z = '大家好，我是{name}，我今年{age}岁了，我来自{addr}'.format(age=18, name='jack', addr='California')
print(z)

# 混合使用 {数字} {变量}
# 要先写数字，再写变量
a = '大家好，我是{name}，我今年{1}岁了，我来自{0}'.format('泰国', 23, name='jerry')
print(a)

# {}什么都不写 {数字} 不能混合使用

d = ['Allen', 18, '上海', 180]
b = '大家好，我是{},我今年{}岁，我来自{}，身高{}'.format(d[1], d[0], d[3], d[2])
# b = '大家好，我是{},我今年{}岁，我来自{}，身高{}'.format(*d)  # 拆包 一一对应
print(b)

info = {'name': 'Chris', 'age': 24, 'addr': 'New York', 'height': 180}
c = '大家好，我是{name}，今年{age}岁了，身高{height}cm，来自{addr}。'.format(**info)
print(c)
