nums = [6, 5, 3, 1, 8, 7, 2, 4]

# 冒泡排序思想：
# 让一个数字和它相邻的下一个数字比较运算
# 如果前一个数字大于后一个数字，交换两个数据的位置
# nums[0] nums[1]
# nums[1] nums[2]
# ... ...
# nums[n] nums[n + 1]
# ... ...
# nums[length - 2] nums[length - 1]

# 每一轮比较次数优化
# 总比较轮数优化

m = 0
while m < len(nums) - 1:  # 每次取最大，最多length - 1次
    m += 1

    i = 0
    while i < len(nums) - 1:  # 第一轮排序
        # print(nums[i], nums[i + 1])
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i += 1

print(nums)

