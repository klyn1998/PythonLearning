# 列表可以使用extend方法将两个列表合并成为一个列表
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9]
nums1.extend(nums2)
print(nums1)
print((nums1 + nums2))


words1 = ('hello', 'good')
words2 = ('happy', 'ok')
print(words1 + words2)  # ('hello', 'good', 'happy', 'ok')

person1 = {'name': 'allen', 'age': 18}
person2 = {'addr': 'Japan', 'height': 180}
person1.update(person2)
print(person1)

# 字典之间不支持加法运算
# print(person1 + person2)
