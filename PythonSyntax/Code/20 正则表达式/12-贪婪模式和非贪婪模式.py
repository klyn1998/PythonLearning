import re

# 在Python的正则表达式里，默认是贪婪模式，尽可能多的匹配
# 非贪婪模式：在满足条件的情况下，尽可能少的匹配
# 在贪婪模式后面添加 ? 可以将贪婪模式转换成为非贪婪模式
m = re.search(r'a.*?b', 'dsakjdbdsebf')
print(m.group())

# 在*, ?, +, {m,n} 后面加上 ? 使贪婪变成非贪婪
print(re.match(r'aa(\d+?)', 'aa1234ddd').group())

print(re.match(r'aa(\d{2,}?)', 'aa1234ddd').group())

print(re.match(r'aa(\d{2,})ddd', 'aa1234ddd').group())
print(re.match(r'aa(\d{2,}?)ddd', 'aa1234ddd').group())

print(re.match(r'aa(\d+?).*', 'aa1234ddd').group(1))

print(re.match(r'aa(\d??)', 'aa1234ddd').group())

src = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
x = re.search(r'https://.*?\.jpg', src)
print(x.group())
