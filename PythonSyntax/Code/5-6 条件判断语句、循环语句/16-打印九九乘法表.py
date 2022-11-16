j = 0
while j < 9:
    j += 1
    i = 0
    while i < j:
        i += 1
        print(i, '*', j, '=', i * j, sep='', end='\t')  # \t 不换行
    print()                                             # print() 换行
