# 101-200所有质数
# for i in range(101, 201):
for i in range(101, 201):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            # 除尽了，说明i是个和数
            flag = False  # i不是质数
            break
    if flag:  # if flag == True
        print(i, '是质数')
