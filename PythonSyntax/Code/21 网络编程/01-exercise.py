import re

# 用户名匹配
# 1. 用户名只能包含数字字母下划线
# 2. 不能以数字开头
# 3. 长度在6-16位范围内

# user_name = input('请输入用户名')
# x = re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]{5,15}', user_name)
# if not x:
#     print('输入的用户名不符合规范')
# else:
#     print(x.group())

# 密码匹配
# 1. 不能包含 !@#¥^%&* 这些特殊符号
# 2. 必须以字母开头
# 3. 长度必须在6到12位之间
# password = input('请输入密码')
# y = re.fullmatch(r'[A-Za-z][^!@#¥%^&*]{5,11}', password)
# if not y:
#     print('输入的密码不规范')
# else:
#     print(y.group())

# 已知有文件text.txt里的内容
# 查找文件中以1000phone开头的语句，并保存到列表中

# try:
#     with open('test.txt') as file:
#         text = file.read()
#         print(re.findall(r'1000phone.*', text))
# except FileNotFoundError:
#     print('文件未找到')

# ipv4格式的ip地址匹配
# IP地址的范围是 0.0.0.0 - 255.255.255.255
# ip = input('请输入IP')
# z = re.fullmatch(r'((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])', ip)
# # print(z)
#
# if not z:
#     print('IP地址不规范')
# else:
#     print(z.group())

# 提取用户输入数据中的数值(数值包括正负数，还包括整数和小数在内)，并求和
# -3.14good87nice19bye  ==> -3.14 + 87 + 19 = 102.86
s = '-3.14go037od87nice19bye'
a = re.finditer(r'-?(0|[1-9]\d*)(\.\d+)?', s)
i_sum = 0
for i in a:
    print(i)
    i_sum += float(i.group())
print(i_sum)
