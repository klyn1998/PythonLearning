# 使用循环计算1-100的计算结果
# i = 0
# result = 0
# while i < 100:
#     i += 1
#     result += i
# print(result)

# r = 0
# for j in range(0, 101):
#     r += j
# print(r)

# 统计100以内个位数是2并且能够被3整除的数的个数
# 取个位数，使用 % 10
# count = 0
# for i in range(1, 101):
#     if i % 10 == 2 and i % 3 == 0:
#         count += 1
# print(count)

# 任意输入一个正整数，求它是几位数
# count = 0
# num = int(input('请输入一个整数：'))
# while True:
#     count += 1
#     num = num // 10  # 整除10 不等于0 取位数
#     if num == 0:
#         break
# print('你输入的数字是', count, '位数', sep='')

# 打印所有水仙花数
# 水仙花数是一个三位数，其各位数字立方和等于该数本身。
# for i in range(100, 1000):  # 456
#     ge = i % 10  # 取个位数
#     shi = i // 10 % 10  # 取十位数
#     bai = i // 100  # 取百位数
#     if ge ** 3 + shi ** 3 + bai ** 3 == i:
#         print(i)

# 写一个程序可以不断的打印内容，如果输入的内容是exit，打印'程序结束'后结束该程序
# while True:
#     content = input('请输入内容：')
#     if content == 'exit':
#         print('程序结束')
#         break
