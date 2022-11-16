class Demo:
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration


d = Demo(10)

a = d.__iter__()
a.__next__()

i = iter(d)  # 内置函数 iter 可以获取到一个可迭代对象的迭代器
print(next(i))
for a in i:  # 迭代器也可以for in 循环
    print(a)
# for x in d:
#     print(x)
