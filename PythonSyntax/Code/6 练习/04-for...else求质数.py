# 质数，不能被除了1和它本身以外的数整除
# 求101-200的质数(1既不是质数，也不是和数)
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:  # i 不是质数
            break  # break放在内循环里，用来结束内循环(j)
    else:
        print(i, '是质数', sep='')
    # else:  # for else语句：当循环里的break没有被执行的时候，就会执行else
    #     print(i, '是质数', sep='')
