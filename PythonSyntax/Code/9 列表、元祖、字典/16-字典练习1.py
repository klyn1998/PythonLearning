persons = [
    {'name': 'zhangsan', 'age': 18},
    {'name': 'lisi', 'age': 20},
    {'name': 'wangwu', 'age': 19},
    {'name': 'jerry', 'age': 21}
]

# 让用户输入姓名，如果姓名已存在，提示用户；如果姓名不存在，继续输入年龄，并存入列表
user_name = input('请输入姓名')
for person in persons:
    if person['name'] == user_name:
        print('姓名已存在')
        break
else:
    # print('姓名不存在')
    user_age = int(input('请输入年龄'))
    persons.append({'name': user_name, 'age': user_age})


print(persons)
