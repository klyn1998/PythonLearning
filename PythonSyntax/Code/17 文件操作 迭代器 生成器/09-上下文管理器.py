# with 语句后面的结果对象，需要重写 __enter__ 和 __exit__ 方法
# 当进入到with代码块时，会自动调用__enter__方法里的代码
# with代码块执行完成之后，会自动调用__exit__方法


class Demo:
    def __enter__(self):
        print('__enter__方法被调用了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了')


# x = Demo()
# d = x.__enter__()
with Demo() as d:
    # 变量d 不是 Demo() 创建的对象
    # 它是创建的对象调用__enter__之后的返回结果
    print(d)
