# 字母表示它本身，很多字母前 \ 会有特殊含义
import re

# \s 表示任意的空白字符
print(re.search(r'\s+', 'hello \n\tworld'))  # 空格、换行、制表符

# \S 表示非空白字符
print(re.search(r'\S', '\t\n   x'))

# \n 表示换行  \t表示一个制表符 \s空白字符 \S 非空白字符

# \d: 表示数字，等价于[0-9]
print(re.search(r'x\d+p', 'x243p'))

# ^ 除了表示以指定的内容开始，在 [] 还可以表示取反
# \D 表示非数字，等价于[^0-9]
print(re.search(r'\D+', 'he999'))
print(re.search(r'[^0-9]+', 'he999'))

# \w：表示数字、字母、_ 以及中文等  非标点符号
print(re.findall(r'\w+', 'h+E-99.2_X*.+-'))
print(re.findall(r'\w+', '大+家-好'))  # 可以取中文

# \W: \w 取反
print(re.findall(r'\W+', 'h+E-99.2_X*.+-'))
