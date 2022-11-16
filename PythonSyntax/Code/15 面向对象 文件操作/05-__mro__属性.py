class A(object):
    pass


class B(object):
    def foo(self):
        print('我是B里的foo')


class C(A):
    def foo(self):
        print('我是A里的foo')


class D(B):
    pass


class X(D, C):
    pass


x = X()
x.foo()  # 我是B里的foo
print(X.__mro__)
# (<class '__main__.X'>, <class '__main__.D'>, <class '__main__.B'>,
# <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
