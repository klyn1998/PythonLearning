user_list = [
    {'name': 'allen', 'tel': '188', 'tg': '222'},
    {'name': 'bob', 'tel': '3456', 'tg': '437895'},
    {'name': 'cindy', 'tel': '1538', 'tg': 'u8906'}
]


def check_number(index):
    if not index.isdigit():
        print('不是数字')
        return False
    index = int(index)
    if not 0 <= index <= len(user_list) - 1:
        print('该用户不存在')
        return False
    return True


def add_user():
    name = input('请输入姓名：')
    for u in user_list:
        if u['name'] == name:
            print('用户名已经被占用')
            return

    tel = input('请输入电话：')
    tg = input('请输入telegram id')
    user = {'name': name, 'tel': tel, 'tg': tg}
    user_list.append(user)


def delete_user():
    number = input('请输入要删除的序号')
    if not check_number(number):
        return
    number = int(number)
    user_list.pop(number)


def change_user():
    number = input('请输入需要修改的用户的序号')
    if not check_number(number):
        return
    number = int(number)
    user = user_list[number]
    print('需要修改的用户为\nname: {name}, tel: {tel}, tg: {tg}'.format(**user))
    name = input('请输入新的姓名')
    for u in user_list:
        if u['name'] == name:
            print('该用户名已被占用')
            return
    user['name'] = name
    user['tel'] = input('请输入新的电话')
    user['tg'] = input('请输入新的tg')
    print(user_list)


def search_user():
    name = input('请输入需要查询的姓名')
    for u in user_list:
        if u['name'] == name:
            print('查询到的信息如下：\nname: {name}, tel:{tel}, tg: {tg}'.format(**u))
            return
    print('该用户不存在')


def show_all():
    for u in user_list:
        print('name: {name}, tel:{tel}, tg: {tg}'.format(**u))


def exit_system():
    if input('确认要退出吗？y/n').lower() == 'y':
        exit()


def start():
    while True:
        print('名片管理系统 V1.0\n1：添加名片\n2：删除名片\n3：修改名片\n4：查询名片\n5：显示所有名片\n6：退出系统')
        number = input('请选择功能（输入数字）：')
        if number == '1':
            add_user()
        elif number == '2':
            delete_user()
        elif number == '3':
            change_user()
        elif number == '4':
            search_user()
        elif number == '5':
            show_all()
        elif number == '6':
            exit_system()
        else:
            print('输入不合法，请重新输入')


start()
