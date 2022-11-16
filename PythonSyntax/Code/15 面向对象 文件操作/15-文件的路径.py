# open 参数介绍
# file：用来指定打开的文件（不是文件的名字，而是文件的路径）
# mode：打开文件时的模式，默认是 r 表示只读
# encoding：打开文件时的编码方式

# 路径分为两种
# 1. 绝对路径：从电脑盘符开始的路径
# 在非windows系统里，文件夹之间使用 / 分割
# file = open('/Users/chenghao/Documents/pycharm/15/xxx.txt')

# 2. 相对路径：当前文件所在的文件夹开始的路径
# ../ 表示返回到上一级文件夹
# ./ 可以省略不写，表示当前文件夹
# / 不能随便用，macos表示根路径
# file = open('xxx.txt')
file = open('./demo/sss.txt')
# file = open('../哈哈哈哈.txt')
print(file.read())
file.close()

# 多使用相对路径
