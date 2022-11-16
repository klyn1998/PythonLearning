import csv  # 系统内置模块

file = open('demo.csv', 'w')  # 打开一个文件
w = csv.writer(file)
print(w)
w.writerow(['name', 'age', 'score', 'city'])
w.writerow(['allen', '18', '90', 'Shanghai'])
w.writerow(['bob', '20', '93', 'New York'])
w.writerow(['cindy', '22', '80', 'Tokyo'])
w.writerows(
    [
        ['name', 'age', 'score', 'city'],
        ['allen', '18', '90', 'Shanghai'],
        ['bob', '20', '93', 'New York']
    ]
)

# file = open('info.csv', 'r')
# r = csv.reader(file)
# for data in r:
#     print(data)
#
# file.close()
