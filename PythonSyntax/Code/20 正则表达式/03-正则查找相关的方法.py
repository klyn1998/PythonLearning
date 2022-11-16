import re

# 查找相关的方法

# match和search:
# 共同点：1. 只对字符串查询一次  2. 返回值类型都是re.Match类型的对象
# 不同点：1. match是从头开始匹配，一旦匹配失败，就返回None；search是在整个字符串里匹配

# finditer: 查找到所有的匹配数据，放到一个可迭代对象里

# findall: 把查找到的所有字符串结果放到一个列表里

# fullmatch: 完整匹配，字符串需要完全满足正则规则才会有结果，否则就是None


r1 = re.match(r'good', 'hello world good morning')
print(r1)  # None

r2 = re.search(r'good', 'hello world good morning')
print(r2)  # <re.Match object; span=(12, 16), match='good'>

# re.search(r'x', 'safxfadsfxklzx')

# finditer 返回的是一个可迭代对象
# 可迭代对象里的数据是匹配到的所有结果，是一个re.Match类型的对象
r3 = re.finditer(r'x', 'safxfadsfxklzx')
print(r3)  # <callable_iterator object at 0x7fbf8815bfd0>

for r in r3:
    print(r)

r4 = re.findall(r'(x)(\d+)', 'safx2fadsfx99klzx55')
print(r4)  # ['x2', 'x99', 'x55']

r5 = re.fullmatch(r'hello world', 'hello world')
print(r5)
