nums = [6, 5, 3, 1, 8, 7, 2, 4]

j = 0
# 第一趟比较时，j = 0，多比较了0次
# 第二趟比较时，j = 1，多比较了1次
# 第三趟比较时，j = 2，多比较了2次
while j < len(nums) - 1:
    # 在每一趟里都定义一个flag
    flag = True  # 假设每一趟都没有换行
    i = 0
    while i < len(nums) - j:
        if nums[i] > nums[i + 1]:
            # 只要交换了，假设不成立
            flag = False
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i += 1
    if flag:
        # 这一趟走完之后，依然是True，说明没交换
        break
    j += 1
print(nums)
