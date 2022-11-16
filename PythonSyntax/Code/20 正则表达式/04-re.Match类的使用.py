# 调用 re.match、re.search或者对re.finditer结果进行遍历
# 拿到的内容都是re.Match类型的对象
import re

# . 任意字符 * 出现任意次数  贪婪模式 *会尽可能多的匹配
m = re.search('s.*s', 'sdffrms23af')
print(m)
print(m.pos, m.endpos)  # 查询位置
print(m.span())  # 匹配到的结果字符串的开始和结束下标

# 使用group方法获取匹配的字符串结果
# group可以传参，表示第 n 个分组
print(m.group())  # sdffrms
print(m.group(0))
# print(m.group(1))  # IndexError: no such group

# group方法表示正则表达式的分组
# 1. 在正则表达式里使用() 表示一个分组
# 2. 如果没有分组，默认只有一组
# 3. 分组的下标从0开始

# 正则表达式有4个分组
m1 = re.search(r'(9.*)(0.*)(5.*7)', 'da9sfn0fjklm5nmgnd7sml;m')
# 分组0：(9.*)(0.*)(5.*7)
# 第0组就是把整个正则表达式当作一个整体
# 默认就是拿第0组
print(m1.group())
# 分组1：(9.*)
print(m1.group(1))  # 9sfn
print(m1.group(2))  # 0fjklm
print(m1.group(3))  # 5nmgnd7

print(m1.groups())  # ('9sfn', '0fjklm', '5nmgnd7')

# groupdict 是获取到分组组成的字典
# (?P<name>表达式)  可以给分组起一个名字
m2 = re.search(r'(?P<allen>9.*)(?P<bob>0.*)(5.*7)', 'da9sfn0fjklm5nmgnd7sml;m')
print('________')
print(m2.groupdict())

# 可以通过分组名或者分组的下标获取到分组里匹配到的字符串
print(m2.group('allen'))
print(m2.group(1))

print(m2.span('bob'))
