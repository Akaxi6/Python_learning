# 第五章 函数

# 作业：5.2 判断一个整数是否为素数
#      5.3 判断字符类型

# 5.1 基本函数

# 函数定义语法
# def 函数名( [参数列表] )：
# '''注释：函数作用 + 参数说明'''

# 形参不需要指定类型，必须要有括号，注意：冒号，def后面必须要有空格，Python允许嵌套函数

def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=" ")
        a, b = b , a+b
    print()

fib(100)

# 可以使用嵌套函数

# 递归

class linear:
    def __init__(self, a, b):
        self.a, self.b = a, b
    def __call__(self, x):
        return self.a * x + self.b

taxk = linear(5, 3)

# 修饰器 @

# 函数递归调用

# eg.因数分解
from random import randint

'''def factors(num, fac=[]):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            fac.append(i)
            factors(num//i, fac)
            break
    else:
        a = 1

factors(5, m[])
'''

# 5.2 函数的参数

# 实参是可变序列，函数会改变

# 位置参数
# 默认值参数 (.... , times = 1)

def say(a, times = 1):
    a + times

print(say.__defaults__) # 查看默认值

# 函数默认值参数是在函数定义时确定值的，只会被初始化一次

# 关键参数

# 可变长度参数**  parameter
# 在参数名前加1个* -- 用来接受多个参数放在元组里面
# 在参数名前加2个* -- 用来接受多个参数放在字典里面

# 传参的序列解包
def demo (a, b, c):
    print(a+b+c)

seq = [1, 2, 3]
demo(*seq)  # 序列解包 （用一个*对列表进行解包）

dic = {'a': 1, 'b': 2, 'c': 3}
demo(**dic)

# 序列解包相当于位置参数，优先级更高

# 5.3 变量作用域
# 局部变量：在函数内部，速度更快
# 全局变量：global
'''
x = 3
def f():
    print(x)
    x = 5
    print(x)
f()
'''

# 5.4 lambda 表达式

# 用来声明匿名函数

f  = lambda x, y, z: x+y+z
print(f(1, 2, 3))

# map(function, L[])--映射
L = [1, 2, 3, 4, 5]
print(list(map(lambda x: x+10, L)))

# 生成器函数

L = input('请输入一些实数')
def Myget(*L):
    avg = sum(L) / len(L)
    g = [i for i in L if i >avg]
    return (avg,) + tuple(g)

L = input('请输入一些实数')

'''x = 3
def f():
    print(x)
    x = 5
    print(x)
f()'''

