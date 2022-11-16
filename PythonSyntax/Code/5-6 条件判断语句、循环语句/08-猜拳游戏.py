import random

# = 赋值运算符，等号用来赋值
# 判断变量是否相等，使用==比较运算符
player = int(input('请输入（0）剪刀 （1）石头（2）布:'))
print('用户输入的是', player)

# 电脑应该随机的出一个数字 [0,2]
# 需要使用到随机数模块 random
# random.randint(a,b) ==> 能够生成[a,b]的随机整数
computer = random.randint(0, 2)
print('电脑出的是', computer)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print('you win, congratulations!')
elif player == computer:
    print('draw game')
else:
    print('you lose, noob!')
