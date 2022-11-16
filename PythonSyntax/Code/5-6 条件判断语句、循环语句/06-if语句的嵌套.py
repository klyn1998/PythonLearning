# if 语句里再嵌套 if

# Python语言里，使用强制缩进来表示语句之间的结构
# 同层级的缩进对齐
ticket = input('是否买票了？Y/N')
if ticket == 'Y':
    print('买票了，可以进站')
    safe = input('安检是否通过？Y/N')
    if safe == 'Y':
        print('安检通过，进候车室')
    else:
        print('进站了，安检未通过')
else:
    print('未买票')
