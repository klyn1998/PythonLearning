# 学生类 Student
# 属性：学号，姓名，年龄，性别，成绩
# 班级类 Grade
# 属性：班级名称，班级中的学生（使用列表储存学生）
# 方法：
# 1. 查看该班级中的所有学生的信息
# 2. 查看指定学号的学生信息
# 3. 查看班级中成绩不及格的学生信息
# 4. 将班级中的学生按照成绩降序排序

class Student:
    def __init__(self, number, name, age, gender, score):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __repr__(self):
        return str(self.__dict__)


class Grade:
    def __init__(self, name, students=None):
        if students is None:
            students = []
        self.name = name
        self.students = students

    def get_information(self):
        for student in self.students:
            print(student)

    def find_student(self, number):
        for student in self.students:
            if student.number == number:
                print(student)
                break
        else:
            print('用户未找到')

    def failed_students(self):
        result = filter(lambda a: a.score < 60, self.students)
        for x in result:
            print(x)

    def ranking(self):
        self.students.sort(key=lambda a: a.score, reverse=True)  # 直接修改self.students
        # return sorted(self.students, key=lambda a: a.score, reverse=True)


s1 = Student('001', 'allen', 18, 'male', 90)
s2 = Student('005', 'bob', 20, 'female', 92)
s3 = Student('007', 'cindy', 19, 'female', 83)
s4 = Student('010', 'danie', 19, 'female', 42)
s5 = Student('006', 'jack', 21, 'male', 59)

g1 = Grade('二班', [s1, s2, s3, s4, s5])
# g1.get_information()
# g1.find_student('008')
# g1.failed_students()
g1.ranking()
print(g1.students)
# x = g1.ranking()
# for i in x:
#     print(i)
