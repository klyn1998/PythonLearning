# Python里，可以使用一对单引号、一对双引号；或者一对三个双引号、一对三个单引号
a = 'hello'  # 最常用
b = "good"
c = """abandon"""
d = '''bad'''

m = 'allen said:"i am allen"'  # 如果字符串里还有双引号，外面使用单引号
n = "I'm allen."
o = """allen said:"I am allen" """

# 字符串里的转义字符 \
# \' ==> 表示一个普通的单引号
# \" ==> 表示一个普通的双引号
# \t ==> 表示一个制表符
# \n ==> 表示换行
# \\ ==> 表示一个普通的反斜线
# 在字符串的前面添加一个r，表示原生字符串
x = 'I\'m allen'  # \ 表示的是转义字符，作用是对 \ 后面的字符进行转义
y = "allen said:\"I am allen\""
print('hello\nworld')
print('你好\t世界')

e = 'good mor\\ning\\'  # 普通斜杠
print(e)

f = r'hi \teacher'  # 原生字符串
print(f)
