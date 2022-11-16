import file_manager
import model

teacher_name = ''


def add_student():
    x = file_manager.read_json('%s.json' % teacher_name, {})
    if not x:
        students = []
        num = 0
    else:
        students = x['all_students']
        num = int(x['num'])

    while True:
        s_name = input('请输入学生姓名')
        s_age = input('请输入年龄')
        s_gender = input('请输入性别')
        s_tel = input('请输入电话')
        num += 1
        # zfill，在字符串前补0
        s_id = 'stu_' + str(num).zfill(4)

        s = model.Student(s_name, s_age, s_gender, s_tel, s_id)
        students.append(s.__dict__)
        data = {'all_students': students, 'num': len(students)}
        file_manager.write_json('%s.json' % teacher_name, data)
        choice = input('添加成功！\n1. 继续\n2. 返回\n请选择')
        if choice == '2':
            break


def show_student():
    operator = input('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n其它：返回\n请选择：')
    x = file_manager.read_json(teacher_name + '.json', {})
    students = x.get('all_students', [])
    key = value = ''
    if not students:
        print('该老师还没有学员')
        return
    if operator == '1':
        pass
    elif operator == '2':
        value = input('请输入姓名')
        key = 'name'
    elif operator == '3':
        value = input('请输入学号')
        key = 's_id'
    else:
        return

    students = filter(lambda s: s.get(key, '') == value, students)

    if not students:
        print('未找到学员')
        return

    for x in students:
        print('学号：{s_id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**x))


def modify_student():
    pass


def delete_student():
    pass


def show_manager():
    content = file_manager.read_file('students_page.txt') % teacher_name
    while True:
        operator = input(content + '\n请选择(1-5)')
        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            modify_student()
        elif operator == '4':
            delete_student()
        elif operator == '5':
            break
        else:
            print('输入不正确，请重新输入')
