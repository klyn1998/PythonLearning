# 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)

sing = ('李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石')
dance = ('李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄')
rap = ('李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白')
# (1) 求选课学生总共有多少人
# 使用集合set可以去重
students = set(sing + dance + rap)
print(len(students))

# (2) 求只选了第一个学科的人的数量和对应的名字
sing_only = []
for p in sing:
    if p not in dance and p not in rap:
        sing_only.append(p)
print(sing_only)

# (3) 求只选了一门学科的学生的数量和对应的名字
# (4) 求只选了两门学科的学生的数量和对应的名字
# (5) 求选了三门学生的学生的数量和对应的名字
names = {}

all_students = sing + dance + rap
for student in all_students:
    # if student in names:
    #     names[student] += 1
    # else:
    #     names[student] = 1
    if student not in names:
        names[student] = all_students.count(student)
print(names)

student_1 = []
student_2 = []
student_3 = []

for k, v in names.items():
    if v == 1:
        student_1.append(k)
    elif v == 2:
        student_2.append(k)
    elif v == 3:
        student_3.append(k)
print('选了一门课的有{}, 选了两门课的有{}，选了三门课的有{}。'.format(student_1, student_2, student_3))
