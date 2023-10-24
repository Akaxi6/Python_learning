# 编写函数，判断一个整数是否为素数，并编写主程序调用该函数
# 第一种方法

def my_sushu_1(num1):
    '''
    函数作用：判断一个整数是否为素数
    输入：整数num1
    返回：无
    '''
    for i in range(2, num1//2):    # 使用循环来判断，到这个数的一半
        if num1 % i == 0:         # 如果数能够被整除，就不是素数
            print("{0}不是一个素数".format(num1))
            break
    else:     # 否则就是素数
        print("{0}是一个素数".format(num1))


print("第一种方法")
x = int(input("请输入一个数："))
my_sushu_1(x)


# 第二种方法

my_sushu_2 = lambda num2: all(num2 % i != 0 for i in range(2, num2//2))    # 利于匿名函数lambda , all判断是否为全真，如果num2全不能被整除，那就是“真的”素数

print("第二种方法")
y = int(input("请输入一个数："))
if my_sushu_2(y):   # 全不能被整除--素数
    print("{0}是一个素数".format(y))
else:   # 否则就不是素数
    print("{0}不是一个素数".format(y))


# 第三种方法
import math

def my_sushu_3(num3):
    '''
    函数作用：判断一个整数是否为素数
    输入：整数num3
    返回：无
    '''
    for i in range(2, int(math.sqrt(num3)) + 1):    # 使用循环来判断，但是循环条件变成了到这个数开根号+1
        if num3 % i == 0:    # 如果数能够被整除，就不是素数
            print("{0}不是一个素数".format(num3))
            break
    else:
        print("{0}是一个素数".format(num3))

print("第三种方法")
x = int(input("请输入一个数："))
my_sushu_3(x)