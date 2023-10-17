# 第九章 文件内容操作
import struct

# 文本文件 / 二进制文件（字节存储）

# 打开文件 - 读取文件 - 写入文件 - 删除文件

# open(file,   mode = 'r', buffering = -1, encoding = Utf-8)
#      文件路径   模式：读        缓存模式           编码模式
# 文件打开模式：r\w\x\a

f1 = open('hello.py', 'r')    # 读模式
f2 = open('hello.py', 'w')    # 写模式

f1.close()    # 打开后关闭
f1.flush()    # 写入但不关闭
# f1.read([size])    # 读取文件指定字符

f1.readline()    # 读取一行

# f1.write()   # 写入文件

# 上下文管理语句 with

# with open(filename) as xx:

# with open('hello.py') as fp:
#    fp.seek(13)
#    fp.write('nihao')

# 排序整数
with open('data.txt', 'r') as fp:
    data = fp.readline()
data = [line.strip() for line in data]
data = ','.join(data)
data = data.split(',')
data = [int(item) for item in data]
data.sort()
data = ','.join(map(str,data))

# csv文件

# 二进制文件 -- 数据库文件、图像文件、可执行文件、音频视频、office文档等等
# 文件结构序列化

# 标准库 pickle

import pickle
i = 1433223
a = 99.69

# data = (i, a)
with open('sample_pickle.dat', 'wb') as f:    # 注意二进制读写要带b
    try:
        pickle.dump(len(data), f)
        for item in data:
            pickle.dump(item, f)    # 写入

# pickle.load()    # 读取

import shelve
shelve.open('dd', 'rb')

# 使用struct模块写入二进制文件

n = 130000
x = 66.62
b = True
s = '你好'
sn = struct.pack('你好啊', n, x, b)
with open('samlpe.dta', 'wb') as f:
    f.write(sn)
    f.write(s.encode())








