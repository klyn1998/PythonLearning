# 用来处理字符串，对字符串进行检索和替换
# 1. 查找  2. 替换  看身份证格式是否正确
import re

x = 'hello\world'
print(x)
# 在正则表达式里，如果想要匹配一个 \ 需要使用 \\\\

# 第一个参数就是正则匹配规则
# 第二个参数表示需要匹配的字符串

# r = re.search('\\\\', x)

# 还可以在字符串前面加r，\\就表示\\
r = re.search(r'\\', x)

# match 和 search 方法的执行结果是一个Match类型的对象
print(r)  # <re.Match object; span=(5, 6), match='\\'>


