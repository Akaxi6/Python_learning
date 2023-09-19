# Python概述
# 选择题、填空题、程序设计题 【闭卷考试】

# 1.6 标准库与拓展库

import math
x = math.sin(0.5)
print(x)

import random
n = random.random()  # 随机获得[0,1)内的随机数
print(n)

n = random.randint(1, 100)  # 随机获得整数
print(n)

n = random.randrange(1, 100)  # 随机获得整数,是通过函数返回的形式
print(n)

import os.path as path  # os包是专门处理文件的一个包
x = path.isfile(r'C:\windows激活')  # 判断文件是否存在
print(x)


import numpy as np  # 数组处理包numpy，数模专用
a = np.array((1, 2, 3, 4))
print(a)

# 同理也可以用from xx import xx as xx

# 全导入包 *
from math import *
m = gcd(36, 18)  # 最大公约数
print(m)

# 1.7 __name__属性的作用

#def main():
 #   if __name__ == '__main__':   # 定义的函数名字作为__name__属性，函数名字就代替了name
  #      print('This program is run directly')
   # elif __name__ == 'hello':
    #    print('This program is used as a module')

import hello  # 作为模块导入
hello.main()

# 在Python中，__name__是一个内置变量，用于表示当前模块的名称。这个变量在不同的情况下会有不同的值，它的主要作用如下：
# 模块导入时，__name__ 的值是模块的名称：当我们在一个 Python 程序中导入一个模块时，解释器会自动设置被导入模块的 __name__ 变量为该模块的名称。这可用于判断当前模块是以主程序运行还是被导入到其他模块中作为库使用。
# 主程序执行时，__name__ 的值是 "main"：当我们直接执行一个 Python 脚本文件时，解释器会将该脚本作为主程序执行，并将其 __name__ 变量设置为 "main"。我们可以利用这一特性，在脚本中编写一些只在主程序执行时才执行的代码。
# 简而言之，__name__ 可以帮助我们判断模块是作为主程序运行还是被导入为库，并根据情况执行相应的代码。这在编写可重用的模块和测试代码时非常有用。