color = 0xF0384E  # 位运算是将数字当作二进制运算，四个二进制为一组表示一个十六进制
red = color >> 16
print(red)
blue = color >> 8 & 0xFF
green = color & 0xFF
print(hex(red), hex(blue), hex(green))
