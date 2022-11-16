# 1.区间判断
score = float(input('请输入你的成绩'))
# 在某些语言里，判断区间不能连写，需要逻辑运算符来连接 score >= 0 and score < 60
# Python里可以使用连续的区间判断
if 0 <= score < 60:
    print('fail')

# 2.隐式类型转换
if 4:  # if 后面需要的是一个bool类型的值。如果if后面不是bool类型，会自动转换为布尔类型。
    print('hello world')

# 3.三元表达式(对if...else语句的简写)
num1 = int(input('输入数字'))
num2 = int(input('再输入一个数字'))
# if num1 > num2:
#     x = num1
# else:
#     x = num2
x = num1 if num1 > num2 else num2
print('两个数里较大数是', x)
