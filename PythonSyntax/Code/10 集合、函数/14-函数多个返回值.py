def test(a, b):
    x = a // b
    y = a % b

    # 一般情况下，一个函数最多只会执行一个return语句
    # 特殊情况下(finally语句)，一个函数可能会执行多个return语句
    # return x  # return 语句表示一个函数的结束
    # return {'x': x, 'y': y}
    # return [x, y]
    return x, y  # 返回的本质是一个元祖


result = test(13, 5)

# print('商是{}，余数是{}'.format(result['x'], result['y']))

print('商是{}，余数是{}'.format(result[0], result[1]))  # 常用：返回元祖

shang, yushu = test(16, 3)  # 拆包
print('商是{}，余数是{}'.format(shang, yushu))
