import os

file_name = input('请输入一个文件路径')  # sss.txt ==> sss.bak.txt

if os.path.isfile(file_name):  # 判断是否是文件
    # 打开旧文件
    old_file = open(file_name)
    names = file_name.rpartition('.')
    # names = os.path.splitext(file_name)

    # 把旧文件的数据读取出来写入到新的文件
    new_file_name = names[0] + '.bak.' + names[2]
    new_file = open(new_file_name, 'w')  # 打开 一个新文件，用于写入

    new_file.write(old_file.read())

    new_file.close()
    old_file.close()
else:
    print('您输入的文件不存在')
