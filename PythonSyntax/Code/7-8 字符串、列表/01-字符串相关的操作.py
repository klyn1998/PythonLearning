# 面向对象里，我们称之为方法
# 修改大小写
# capitalize 让第一个单词的首字母大写
print('hello world'.capitalize())  # Hello world

# upper 全大写
print('hello'.upper())  # HELLO

# lower 全小写
print('WoRLD'.lower())  # world

# title 每个单词的首字母大写
print('apple to be eaten or pen to be used'.title())

# while True:
#     content = input('请输入内容，输入exit退出:')
#     print('你输入的内容是', content, sep='')
#     if content.lower() == 'exit':
#         break

# ljust(width, fillchar)
# width 长度 fillchar 填充字符，默认是空格
# ljust(length) ==> 让字符串以指定长度显示，如果长度不够，默认在右边使用空格补齐
print('Monday'.ljust(10, '+'))
print('Tuesday'.rjust(12, '-'))
print('Wednesday'.center(20, '+'))

print('++++apple++++'.lstrip('+'))
print('   pear   '.rstrip())
print('    banana   '.strip())

# 以某种固定格式显示的字符串，我们可以将它切割成为一个列表
x = 'allen-bob-catty-doge'
names = x.split('-')
print(names)

# 将列表转换成字符串 join
fruits = ['apple', 'pear', 'peach', 'banana', 'mango']
print(' '.join(fruits))
print('*'.join('hello'))  # 可迭代对象 iterable

# 字符串和运算符
# 字符串和字符串之间可以使用加法运算，作用是拼接两个字符串
print('apple' + 'banana')
# 字符串和数字之间可以使用乘法运算，目的是将指定的字符串重复多次
print('apple' * 9)
# 字符串和数字之间做 == 运算，运算结果是False，做 != 运算，结果是True
# 字符串之间做比较运算，会逐个比较字符串的编码值
# 不支持其他的运算符
