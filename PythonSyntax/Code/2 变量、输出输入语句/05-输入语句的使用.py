# Python里使用 input 内置函数接收用户的输入
# input() ==> 括号里写提示信息
# password = input('请输入银行卡密码：')
# print(password)

# 不管用户输入的是什么，变量保存的都是字符串。
age = input('请告诉我你的年龄')
print(type(age))  # <class 'str'>
# print(age+1) 错误
