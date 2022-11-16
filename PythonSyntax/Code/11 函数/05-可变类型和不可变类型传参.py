def test(a):
    print('修改前a的内存地址0x%X' % id(a))
    a = 100
    # print(a)
    print('修改后a的内存地址0x%X' % id(a))


def demo(nums):
    print('修改前nums的内存地址0x%X' % id(nums))
    nums[0] = 10
    print('修改后nums的内存地址0x%X' % id(nums))


x = 1
print('调用前X的内存地址0x%X' % id(x))
test(x)
print(x)  # 1
print('调用后X的内存地址0x%X' % id(x))

y = [3, 5, 6, 8, 2]
print('调用前Y的内存地址0x%X' % id(y))
demo(y)
print('调用后Y的内存地址0x%X' % id(y))
print(y)
