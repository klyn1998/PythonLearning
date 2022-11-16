import re

# 正则表达式修饰符是对正则表达式进行修饰
# re.S: DOTALL
# . 表示除了换行以外的任意字符
x = re.search(r'd.*a', 'sadgd\nftsa', re.S)
print(x)

# re.I IGNORECASE
y = re.search(r'x', 'good Xyz', re.I)
print(y)

# \w表示的是字母数字和_  +: 出现一次或多次 $:以指定的内容结尾
# re.M：让$能够匹配到换行
z = re.findall(r'\w+$', 'i am boy\nyou are girl\nhe is man', re.M)
print(z)
