class Teacher:
    def __init__(self, name, password):
        import tools
        self.name = name
        self.password = tools.encrypt_password(password)


class Student:
    def __init__(self, name, age, gender, tel, s_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel
        self.s_id = s_id
