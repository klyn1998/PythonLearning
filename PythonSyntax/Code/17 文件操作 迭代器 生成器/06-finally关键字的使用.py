file = open('/Users/chenghao/Downloads/Telegram Desktop/9月1日 (2).mp4', 'rb')
try:
    while True:
        content = file.read(1024)
        print(content)
        if not content:
            break
finally:
    file.close()
    print('文件已关闭')
