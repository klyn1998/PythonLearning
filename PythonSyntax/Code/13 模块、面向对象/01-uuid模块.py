# uuid用来生成一个全局唯一的id
import uuid

print(uuid.uuid1())  # 32个长度，每一个字符有16个选择
# print(uuid.uuid2())  # Python里不能用

# uuid3和uuid5是使用传入的字符串根据指定的算法算出来的，是固定的
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'allen'))  # 生成固定的uuid
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'allen'))  # 生成固定的uuid

print(uuid.uuid4())  # 使用最多，基于随机数
