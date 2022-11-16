# 求1-100的所有整数之和
# x = 0
# result = 0  # 定义一个变量用来保存所有数字之和
# while x < 100:
#     x += 1
#     result = result + x
# print(result)

# 求1-100所有偶数的和
# x = 0
# result = 0  # 定义一个变量用来保存所有数字之和
# while x < 100:
#     x += 1
#     if x % 2 == 0:  # 偶数才被加到result
#         result += x
# print(result)

# 求[35,987]之间所有整数的和
m = 34
n = 0
while m < 987:
    m += 1
    n += m
print(n)
