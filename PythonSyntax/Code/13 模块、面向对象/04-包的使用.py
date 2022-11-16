# 可以将多个具有相似或者有关联的模块放到一个文件夹里，便于统一管理
# 这个文件夹，我们称之为包
# Python包里，会有一个__init__.py 文件
from chat import recv_msg
from chat.send_msg import x
import chat

print(recv_msg.y)
print(x)
print(chat.recv_msg.y)
