# sys 系统相关的功能
import sys

print('hello world')
print('allen')

# ['/Users/chenghao/Documents/pycharm/12',
#  '/Users/chenghao/Documents/pycharm/12',
#  '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
#  '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
#  '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
#  '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
#  '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages',
#  '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']
print(sys.path)  # 结果是一个列表，表示查找模块的路径

# sys.stdin  # 可以像input一样，接受用户的输入
# sys.stdout  # 标准输出，修改sys.stdout，可以改变默认输出位置
# sys.stderr  # 修改sys.stderr，可以改变错误输出的默认位置

sys.exit(100)  # 程序退出，和内置函数exit功能一致
