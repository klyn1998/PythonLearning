for i in range(101, 201):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i, '是一个质数', sep='')
    else:
        print(i, '是一个和数,', '它能被', count, '个数字整除', sep='')
