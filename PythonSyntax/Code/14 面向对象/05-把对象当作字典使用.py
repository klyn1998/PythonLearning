class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        print('key: {}, value: {}'.format(key, value))
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person('allen', 18)
print(p.__dict__)  # 将对象转换成为字典{'name': 'allen', 'age': 18}

# 不能直接把一个对象当作字典来使用
p['name'] = 'jack'  # []语法会调用对象的 __setitem__ 方法
print(p.name)

print(p['name'])  # 会调用  __getitem__ 方法
print(p.__dict__['name'])
