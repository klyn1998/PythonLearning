# 在re模块里，可以使用re.方法调用函数，也可以使用re.compile得到一个对象
import re

# 可以直接调用re.search方法
s = re.search(r'd.*k', 'dsfgjbka')
print(s)

c = re.compile(r'd.*k')  # 规定正则规则；效果一样
x = c.search('dsfgjbka')
print(x)
