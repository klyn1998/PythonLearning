import file_manager
import model
import tools


def login():
    data = file_manager.read_json('data.json', {})
    teacher_name = input('请输入教师账号')
    if teacher_name not in data:
        print('账号不存在')
        return
    password = input('请输入密码')
    if tools.encrypt_password(password) == data[teacher_name]:
        import student_manager
        student_manager.teacher_name = teacher_name
        student_manager.show_manager()
    else:
        print('密码不正确，登录失败！')


def register():
    # 读取文件，查看文件里是否有数据。如果文件不存在，默认是一个字典
    data = file_manager.read_json('data.json', {})
    while True:
        teacher_name = input('请输入账号(3~6位)')
        if not 3 <= len(teacher_name) <= 6:
            print('账号不符合要求，请重新输入')
        else:
            break

    if teacher_name in data:
        print('该账号已存在！')
        return

    while True:
        password = input('请输入密码(6~12位)')
        if not 6 <= len(password) <= 12:
            print('密码不符合要求，请重新输入')
        else:
            break

    # 用户名密码都已经输入正确，创建一个teacher对象
    t = model.Teacher(teacher_name, password)
    data[t.name] = t.password
    file_manager.write_json('data.json', data)


def start():
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '\n请输入数字(1~3)')
        if operator == '1':
            login()
        elif operator == '2':
            register()
        elif operator == '3':
            break
        else:
            print('输入有误！')


if __name__ == '__main__':
    start()
