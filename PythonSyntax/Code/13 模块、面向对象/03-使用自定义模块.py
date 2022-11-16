# 一个模块本质上就是一个py文件
# 自己定义一个模块，其实就是自己写一个py文件

# import 04-My Module
# 如果一个py文件想要被当作一个模块被导入，文件名一定要遵守命名规范
# 由数字、字母、下划线组成，不能以数字开头

import my_module
# 导入了一个模块，就能使用这个模块里变量和方法


from demo import *  # 会执行里面的所有语句

# from <module_name> import *  导入这个模块里'所有'的变量和函数
# 本质是读取模块里的__all__属性，看这个属性里定义了哪些变量和函数
# 如果模块里没有定义__all__，才会导入所有不以 _ 开头的变量和函数


print(my_module.a)
my_module.test()

# 使用from demo import * 写法，不再需要写模块名
print(m)
test()
# print(n)

import demo  # 无限制
print(demo.n)

from hello import *
print(x, y)
# print(_age)

import hello

# print(hello._age)
# hello._bar()
