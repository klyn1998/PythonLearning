# try...except语句用来处理程序运行过程中的异常

try:
    person = {'name': 'allen'}
    print(person['age'])
    print(1 / 2)
    file = open('ddd.txt')
    print(file.read())
    file.close()
# except Exception as e:  # 给异常起了一个变量名e
#     print(e)
# except:
#     print('出错了')
except (FileNotFoundError, ZeroDivisionError, KeyError) as e:  # 处理指定类型的异常
    print(e)
