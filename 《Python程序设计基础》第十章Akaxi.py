import os
import os.path
# 文件与文件夹操作

# os模块

# name chdir(path) environ
print(os.getcwd())
# listdir()

# remove(path)    # 删除文件

# rename(src, dst)    # 重命名文件

# . 当前目录  .. 两个点上一层目录

# os.mkdir(os.getcwd() + '\\temp')    # 创建目录
# os.chdir(os.getcwd() + '\\temp')    # 改变目录

# os.listdir('.')    # 当前所有目录

# 文件目录遍历  -- 深度优先 / 广度优先

from os import listdir
from os.path import join, isfile, isdir

def listDirDepthFirst(directory):
    '''深度优先'''
    for subpath in listdir(directory):
        path = join(directory, subpath)
        if isfile(path):    # 如果是文件
            print(path)
        elif isdir(path):    # 如果是文件夹
            print(path)
            listDirDepthFirst(path)


os.listdir()    # 列举文件

# os.path -- 路径拼接、路径拆分、相对路径提取、文件存在性判断

# isdir()  isfile()  join()  split()以最后一个\\作为划分

# 文件目录打乱

# 磁盘配额




