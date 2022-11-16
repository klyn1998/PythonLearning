chars = ['a', 'c', 'x', 'd', 'c', 'p', 'a', 'p', 'a', 'c']
char_count = {}

for char in chars:
    # 1
    # if char in char_count:  # in运算符用在字典上，用来判断key是否存在，而不是value
    #     char_count[char] += 1
    # else:
    #     char_count[char] = 1

    # 2
    if char not in char_count:
        char_count[char] = chars.count(char)

# 可以使用内置函数max取最大数
vs = char_count.values()
max_count = (max(vs))  # 3

for k, v in char_count.items():
    if v == max_count:
        print(k)

print(char_count)
