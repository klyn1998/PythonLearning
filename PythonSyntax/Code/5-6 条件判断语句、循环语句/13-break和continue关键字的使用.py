# break和continue在Python里只能用在循环语句里

# break：用来结束整个循环
# continue:用来结束本轮循环，开启下一轮循环
# i = 0
# while i < 5:
#     if i == 3:
#         i += 1
#         continue  # 看到continue，就回到头部判断条件，后面的代码就不走了
#     print(i)
#     i += 1

# i = 0
# while i < 5:
#     if i == 3:
#         i += 1
#         break  # break结束全部循环
#     print(i)
#     i += 1

# 不断的询问用户，do u love me，只要答案不是yes，就一直问

# 不断的让用户输入用户名和密码，只要admin不是allen，password不是123，就一直问

answer = input('do u love me?:')
while answer != 'yes':
    answer = input('do u love me?:')


# admin = input('admin')
# password = input('password')
# # while admin != 'allen' and password != '123':  # False就不走了，对一个就不走了
# # 逻辑陷阱: == and == 的否定不是 != and !=
# while not (admin == 'allen' and password == '123'):  # 逻辑取反
#     admin = input('admin')
#     password = input('password')

# while True:
#     admin = input('admin')
#     password = input('password')
#     if admin == 'allen' and password == '123':
#         break

# while True:
#     answer = input('do u love me?')
#     if answer == 'yes':
#         break
