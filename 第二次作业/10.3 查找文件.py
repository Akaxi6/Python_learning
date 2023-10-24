# 编写程序，用户输入一个目录和一个文件名，搜索该目录及其子目录中是否存在该文件

import os


def My_search(path, filename):
    for root, dirs, files in os.walk(path):    # 遍历文件夹下文件并获得路径
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
        if filename in files:    # 找到了文件
            print('在目录{0}中，找到了文件{1}'.format(root, filename))
            break
    else:
        print('在{0}该目录及其子目录中，没有找到文件{1}'.format(path, filename))


x = input("请输入要搜索的目录：")
y = input("请输入要搜索的文件名：")
My_search(x, y)
