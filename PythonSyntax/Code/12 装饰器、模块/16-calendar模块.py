import calendar  # 日历模块

calendar.setfirstweekday(4)  # 设置每周起始日期码，周一到周日分别对应0~6
print(calendar.firstweekday())  # 返回当前每周起始日期的设置。默认情况下，首次载入calendar模块时返回0，即周一

c = calendar.calendar(2022)  # 生成2022年的日历
print(c)

print(calendar.isleap(1999))  # 闰年返回True，否则返回False
print(calendar.leapdays(1873, 1990))  # 获取两个年份之间一共有多少个闰年

print(calendar.month(2022, 10))
