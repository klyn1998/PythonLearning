# 一张纸的厚度大约是0.08mm，对折多少次后能达到珠穆朗玛峰的高度8848.13m
p = 0.08
z = 8848.13 * 1000
i = 0
while True:
    i += 1
    p *= 2
    if p > z:
        break
print(i)
