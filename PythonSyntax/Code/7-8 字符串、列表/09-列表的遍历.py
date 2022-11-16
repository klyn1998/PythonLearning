# 遍历：将所有的数据都访问一遍；遍历针对的是可迭代对象
# while循环遍历 / for...in循环遍历
americans = ['jimmy', 'saul', 'kim', 'mike', 'white', 'kim']

# for...in循环的本质就是不断调用next方法查找下一个数据
for american in americans:
    print(american)

i = 0
while i < len(americans):
    print(americans[i])
    i += 1
