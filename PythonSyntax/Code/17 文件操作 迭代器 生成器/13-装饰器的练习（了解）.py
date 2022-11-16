user_permission = 5  # 0101

# 权限因子
del_permission = 8  # 1000
read_permission = 4  # 0100
write_permission = 2  # 0010
exe_permission = 1  # 0001


def check_permission(x, y):
    def handle_action(fn):
        def do_action():
            if x & y != 0:  # 有权限，可以执行
                fn()
            else:
                print('无该权限')

        return do_action

    return handle_action


@check_permission(user_permission, del_permission)
def delete():
    print('可以删除内容')


@check_permission(user_permission, read_permission)
def read():
    print('可以读取内容')


@check_permission(user_permission, write_permission)
def write():
    print('可以写入内容')


@check_permission(user_permission, exe_permission)
def execute():
    print('可以执行内容')


delete()
read()
write()
execute()
