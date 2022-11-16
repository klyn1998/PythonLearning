score = float(input('请输入你的成绩'))

# 多个if语句，语句和语句之间不存在关联
# if 0 <= score < 60:
#     print('不及格')
#
# if 60 <= score < 80:
#     print('中等')
#
# if 80 <= score < 90:
#     print('良好')
#
# if 90 <= score < 100:
#     print('优秀')

# 一个if...elif 语句
if 0 <= score < 60:
    print('不及格')
elif 60 <= score < 80:
    print('中等')
elif 80 <= score < 90:
    print('良好')
elif 90 <= score <= 100:
    print('优秀')
else:
    print('无效')
