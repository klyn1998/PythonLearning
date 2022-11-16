students = [
    {'name': '张三', 'age': 18, 'score': 52, 'tel': '1388888998', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 89, 'tel': '1388666666', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 95, 'tel': '1365588889', 'gender': 'unknown'},
    {'name': 'jerry', 'age': 20, 'score': 90, 'tel': '156666789', 'gender': 'unknown'},
    {'name': 'chris', 'age': 17, 'score': 98, 'tel': '13777775523', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52, 'tel': '13999999928', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 98, 'tel': '1388888888', 'gender': 'unknown'}
]

# (1) 统计不及格学生的个数
# (2) 打印不及格学生的名字和对应的成绩
# (3) 统计未成年学生的个数
# (4) 打印手机尾号是8的学生的名字
# (5) 打印最高分和对应的学生的名字
# (6) 删除性别不明的所有学生
# (7) 将列表按学生成绩从小到大排序

# 1, 2, 3, 4
count_fail = 0
count_age = 0
for student in students:
    if student['score'] < 60:
        count_fail += 1
        print('%s不及格，分数是%d' % (student['name'], student['score']))
    if student['age'] < 18:
        count_age += 1
    # if student['tel'].endswith('8'):
    if student['tel'][-1] == '8':
        print('手机尾号是8的学生是%s' % student['name'])
print('不及格的学生有%d个' % count_fail)
print('未成年的学生有%d个' % count_age)

# 5
max_grade = students[0]['score']
for student in students:
    if student['score'] > max_grade:
        max_grade = student['score']
print('最高成绩是%d' % max_grade)

for student in students:
    if student['score'] == max_grade:
        print('最高分是%s' % student['name'])

# 6
# 方法1
# i = 0
# while i < len(students):
#     if students[i]['gender'] == 'unknown':
#         print(i)
#         students.pop(i)
#         i -= 1
#     i += 1
# print(students)

# 方法2
# students2 = []
# for student in students:
#     if student['gender'] != 'unknown':
#         students2.append(student)
# students = students2
# print(students)
# 等同于：
# students2 = [student for student in students if student['gender'] != 'unknown']
# print(students2)

# 方法3 students[:]是students的切片，所以修改students对切片无影响
for student in students[:]:
    if student['gender'] == 'unknown':
        students.remove(student)
print(students)

# 7
# m = 0
# while m < len(students) - 1:
#     m += 1
#     n = 0
#     while n < len(students) - 1:
#         if students[n]['score'] > students[n + 1]['score']:
#             students[n], students[n + 1] = students[n + 1], students[n]
#         n += 1
# print(students)

for j in range(0, len(students) - 1):
    for i in range(0, len(students) - 1):
        if students[i]['score'] > students[i + 1]['score']:
            students[i], students[i + 1] = students[i + 1], students[i]
print(students)
