# 正则表达式作用是对字符串进行检索和替换
# 检索：match, search, findall, finditer, fullmatch
# 替换：sub
import re

s = 'sad87f9sd998fa'

print(re.sub(r'\d', 'x', s))  # sadxxfxsdxxxfa
print(re.sub(r'\d+', 'x', s))  # sadxfxsdxfa

# 第一个参数是正则表达式
# 第二个参数是新字符或者一个函数
# 第三个参数是需要被替换的原来的字符串
p = 'hello37good23'  # 把字符串里的数字 *2


# def test(x):
    # print(x)


# sub内部在调用test方法时，会把每一个匹配到的数据以re.Match的格式传参
# print(re.sub(r'\d', test, p))  # 传finditer的迭代结果

print(re.sub(r'\d+', lambda x: str(int(x.group()) * 2), p))
