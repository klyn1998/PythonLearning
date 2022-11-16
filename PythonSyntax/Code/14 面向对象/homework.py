# 编写一个函数，求多个数中的最大值
import random


def get_max(*args):
    x = args[0]
    for arg in args:
        if x < arg:
            x = arg
    return x


print(get_max(1, 2, 4, 6, 6, 8))


# 编写一个函数，实现摇骰子的功能，打印N个骰子的点数之和
def dice(n):
    a = 0
    for i in range(n):
        x = random.randint(1, 6)
        print('第%d次的点数是%d' % (i + 1, x))
        a += x
    print('总点数是%d' % a)


dice(4)


# 编写一个函数，交换指定字典的key和value
def exchange(dict1):
    dict2 = {}
    for k, v in dict1.items():
        dict2[v] = k
    return dict2


person = {'name': 'dd', 'age': 18}
print(exchange(person))


# 编写一个函数，提取指定字符串中所有的字母，然后凭借在一起产生一个新的字符串
def extract(a):
    new_word = ''
    for i in a:
        if i.isalpha():
            new_word += i
    return new_word


print(extract('good213'))


# 写一个函数，求多个数的平均值
def average(*args):
    add = 0
    for arg in args:
        add += arg
    return add / len(args)


print(average(1, 2, 3, 4, 5))


# 写一个函数，默认求10的阶乘，可以求其他数字的阶乘
def factorial(num=10):
    a = 1
    for i in range(1, num + 1):
        a *= i
    return a


print(factorial())


# 写一个自己的capitalize函数，能够将指定字符串的首字母变成大写字母
def my_capitalize(word):
    if word[0].isalpha:
        return word[0].upper() + word[1:]
    return word


print(my_capitalize('111good'))


# 写一个自己的endswith函数，判断一个字符串是否以指定的字符串结束
def my_endswith(word, alpha):
    # 包左不包右；右边从-1开始数
    return word[-len(alpha):] == alpha


print(my_endswith('good', 'od'))


# 写一个自己的isdigit函数，判断一个字符串是否是纯数字字符串
def my_isdigit(nums):
    for i in nums:
        if not '0' <= i <= '9':  # 字符串比较ASCII码
            return False
    return True


print(my_isdigit('898jjj'))


# 写一个自己的upper函数，将一个字符串中所有的小写字母变成大写字母
def my_upper(word):
    new_word = ''
    for i in word:
        if 'a' <= i <= 'z':
            upper_i = chr(ord(i) - 32)
            new_word += upper_i
        else:
            new_word += i
    return new_word


print(my_upper('2uh3h'))


# 写一个自己的 rjust 函数，创建一个字符串的长度是指定长度
# 原字符串在新字符串中右对齐，剩下的部分用指定的字符填充
def my_rjust(word, length, character):
    new_word = ''
    if len(word) >= length:
        return word
    else:
        new_word = new_word + (length - len(word)) * character + word
    return new_word


print(my_rjust('ss', 1, '*'))


# 写一个自己的index函数
# 统计指定列表中指定元素的所有下标，如果列表中没有指定元素返回-1
def my_index(item, items):
    index = []
    for m, n in enumerate(items):
        if n == item:
            index.append(m)
    if index == []:
        return -1
    return index


names = ['allen', 'bob', 'jack', 'mike', 'jimmy', 'bob']
print(my_index('allen', names))


# 写一个自己的len函数，统计指定序列中元素的个数
def my_len(items):
    count = 0
    for i in items:
        count += 1
    return count


nums1 = [1, 2, 3]
print(my_len(nums1))


# 写一个函数实现自己的in操作，判断指定序列中，指定的元素是否存在
def my_in(item, items):
    for i in items:
        if i == item:
            return True
    return False


print(my_in('a', names))


# 写一个自己的replace函数，将指定字符串中的旧字符转换成指定的新字符串
# 1.
# def my_replace(sentence, word1, word2):
#     a = sentence.split(word1)
#     return word2.join(a)


# 2.
def my_replace(sentence, word1, word2):
    result = ''
    i = 0
    while i < len(sentence):
        if sentence[i:i + len(word1)] != word1:
            result += sentence[i]
            i += 1
        else:
            result += word2
            i += len(word1)
    return result


print(my_replace('how are you and you', 'you', 'me'))


# 写一个自己的max函数，获取指定序列中元素的最大值
# 如果序列是字典，取字典值的最大值
def my_max(items):
    if type(items) == dict:
        items = list(items.values())  # 不能直接取值，但能够遍历
    big = items[0]
    for i in items:
        if i > big:
            big = i
    return big


d = [1, 54, 5, 5, 6, 7, 2, 10]
b = 'ssnknazhouh'
c = {'allen': 90, 'bob': 11, 'cindy': 98, 'doge': 32}
print(my_max(c))
