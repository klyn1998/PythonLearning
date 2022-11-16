# 去重排序
nums = [5, 8, 7, 6, 4, 1, 3, 5, 1, 8, 4]
n1 = set(nums)
print(n1)

n2 = list(n1)
n2.sort()
print(n2)

