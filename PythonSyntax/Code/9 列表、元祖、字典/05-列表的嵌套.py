import random

nums = [1, 2, [100, 200, 500], 3, 4, 5]
# 一个学校，有三个办公室，现在有八位老师等待工位的分配，请编写程序，完成随机的分配
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rooms = [[], [], []]
for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)

# 第1个房间里有...个人，分别是...
# 带下标通常使用while
# for循环也可以带下标
for i, room in enumerate(rooms):
    print('房间%d里有%d个老师，分别是' % (i, len(room)), end='')
    for teacher in room:
        print(teacher, end=' ')
