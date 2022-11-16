import re

# 1. 数字和字母都表示它本身
# 2. 很多字母前面添加 \ 会有特殊含义(🌟)
# 3. 绝大多数标点符号都有特殊含义(🌟)；如果使用标点，需要加\

# 字母x表示它本身
re.search(r'x', 'hello xyz')
re.search(r'5', '54904-052')

print(re.search(r'd', 'good'))  # 字母d是普通的字符
print(re.search(r'\d', 'good'))  # \d不再表示字母d
print(re.search(r'\d', 'go4od'))

print(re.search(r'\+', '1 + 2'))
