# 根据输入的百分制成绩打印'及格'或'不及格'，60分以下为不及格
# score = float(input('请输入你的成绩：'))
# if 0 <= score < 60:
#     print('不及格')
# elif 60 <= score <= 100:
#     print('及格')
# else:
#     print('成绩无效')

# 根据输入的年龄打印'成年'或者'未成年'，18岁以下为未成年，如果年龄不在正常范围（0-150）则打印'这不是人'
# age = int(input('请输入你的年龄：'))
# if 0 <= age < 18:
#     print('未成年')
# elif 18 <= age <= 150:
#     print('成年')
# else:
#     print('这不是人')

# 输入两个整数，如果两个数相减的结果为奇数则输出该结果，否则输出提示信息'结果不是奇数'
# num1 = int(input('请输入第一个整数:'))
# num2 = int(input('请输入第二个整数:'))
# if (num1 - num2) % 2 != 0:
#     print(num1 - num2)
# else:
#     print('结果不是奇数')
#
# 使用for循环输出0-100所有的奇数
for i in range(0, 101):
# print(i)   # 打印所有数字
    if i % 2 != 0:  # 奇数才打印
        print(i)
    if i % 2 == 0:  # 偶数就不打印
        continue

# 使用while循环输出0-100内所有的偶数
# j = 0
# while j <= 100:
#     if j % 2 == 0:
#         print(j)
#     j += 1
