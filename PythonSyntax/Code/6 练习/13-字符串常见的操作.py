x = 'abcdefghijklmnl'

# 使用内置函数len 可以获取字符串的长度
print(len(x))

# 查找内容相关的方法 find/index/rfind/rindex  可以获取指定字符的下标
print(x.find('l'))  # 11 找最小的下标
print(x.index('l'))  # 11

print(x.find('p'))  # -1  如果字符在字符串里不存在，结果是-1
# print(x.index('p'))  # 使用index，如果字符不存在，会报错

print(x.find('l', 4, 9))  # -1

print(x.rfind('l'))  # 找最大的下标
print(x.rindex('l'))

# startswith,endswith,isalpha,isalnum,isdigit,isspace
# is开头的是判断，结果是一个布尔类型
print('hello'.startswith('he'))  # True
print('hello'.endswith('o'))  # True
print('123hello'.isalpha())  # False 判断是否是字母
print('good'.isdigit())  # False
print('123'.isdigit())  # True

# alnum 判断是否由数字和字母组成
print('1234ab'.isalnum())  # True
print('1234'.isalnum())  # True
print('ab'.isalnum())  # True
print('4 - 1'.isalnum())  # False

print('    '.isspace())  # True

# 整数的判断
# num = input('请输入一个数字：')
# if num.isdigit():
#     num = int(num)
# else:
#     print('您输入的不是一个数字')

# replace方法：用来替换字符串
word = 'hello'
word_1 = word.replace('l', 'x')  # replace 将字符串里 l 替换成 x
print(word)  # hello 字符串是不可变类型！
print(word_1)  # hexxo 原来的字符串不会改变，而是生成一个新的字符串来保存替换后的结果
