import re

# 标点符号的使用
# ()：用来表示一个分组
m = re.search(r'g(\d+)r', 'safg284rdsa')
print(m.group(1))
# 如果要表示括号，使用 \
n = re.search(r'\(.*\)', '(1 + 1) * 3')
print(n.group())  # (1 + 1)

# . 表示匹配 \n 之外的任意字符。如果想要匹配 . 需要使用 \.

# []  用来表示可选项范围 [x-y] 从x到y区间，包含x和y
# print(re.search(r'o[0-5]+d', 'dsgjio4423daj'))
# print(re.search(r'o[a-d]d', 'dsgjiobdaj'))
print(re.search(r'o[0-5a-dx]+d', 'dsgjioxdaj'))  # 0-5或a-d或x

# | 用来表示或者，和 [] 有一定相似，但是有区别
# []里的值表示的是区间，而且是单个字符
# | 就是可选值，可以出现多个字符
print(re.search(r'f(x|pk|t)m', 'fxpdsfpkm'))

# {} 用来规定前面元素出现的次数
# {n}: 表示前面的元素出现n次
# {n,}: 表示前面的元素出现 n 次及以上
# {,n}: 表示前面的元素出现 n 次及以下
# {m,n}: 表示前面的元素出现m到n次
print(re.search(r'go{3,5}d', 'goooood'))

# *：表示前面的元素出现任意次数（0次及以上），等价于{0,}
print(re.search(r'go*d', 'gd'))

# +：表示前面的的元素至少出现一次，等价于{1,}
print(re.search(r'go+d', 'god'))

# ?：两种用法：
# 1. 规定前面的元素最多只能出现一次，等价于{0,1}
# 2. 将贪婪模式转换成为非贪婪模式
print(re.search(r'go?d', 'gd'))

# ^：以指定的内容开头   $：指定内容结尾
print(re.search(r'^a.*h$', 'afsjklfdh'))
print(re.search(r'^a.*h$', 'rrr\nafsjklfdh\nppp', re.M))
