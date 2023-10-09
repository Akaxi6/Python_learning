# 第二章【运算符、表达式、内置对象】
# 2.1 Python常用内置对象
x = 3
print(type(x))
print(type(x) == int)
print(isinstance(x, int))

x = 'Hello world'  # 字符串
x = [1, 2, 3]   # 列表

x = 3 # 创建变量
print(x**2) # 访问变量的值

x+= 6  # 修改变量的值
print(x)

x = [1, 2, 3]  # 创建列表
print(x)
x[1] = 5  # 修改列表 列表标签从0开始
print(x)

print(x[2])

# 数字
print(99**9)
print(0.3+0.2)
print(0.4-0.1)   # 实数相减会有偏差

print(0.4-0.3 == 0.1)  # 实数相减会有误差，判断相等就不成立
print(abs(0.4-0.3-0.1) < 1e-6)  # 等式变换abs是绝对值，1e-6是10的-6次方

# 虚数
x = 3+4j
y = 5+6j
print(x+y)  # 复数相加
print(x*y)  # 复数相乘
print(abs(x))  # 取模，复数的长度
print(x.imag)  # 复数的虚部
print(x.real)  # 复数的实部
print(x.conjugate())  # 复数的共轭复数

# 分数
from fractions import Fraction  # 导入分数包
x = Fraction(3, 5)
y = Fraction(3, 7)
print(x)
print(y)

print(x**2)
print(x.numerator)  # 分子
print(x.denominator)  # 分母

print(x+y)  # 通分相加

# 高精度实数

from fractions import Decimal
print(1/9)

# 字符串与字节串

x = 'Hello'
print(x)

x = "Hello"
print(x)

x = '''Tom said,"Let's go"'''    # 三个'''中间即可以引用
print(x)

x = 'good ' + 'morning'    # 字符串相加
print(x)

x = 'good '
y = x + ' morning'
print(y)

print(type('Hello'))    # 字符串类型

print(type(b'Hello'))    # 字节串类型，加一个b表示强制转换

print('Hello'.encode('utf-8'))    # 用utf-8的编码格式队Hello字符串进行强制编码->字节串

print('Good'.encode('gbk'))    # 用gbk的编码格式队Hello字符串进行强制编码->字节串

print('王忠全'.encode('utf-8'))    # 对中文用utf-8格式编码后输出的是\xe7这样的字节串

print('王忠全'.encode('gbk'))    # 对中文用gbk格式u编码后输出的是\xe7这样的字节串，不同于utf-8的编码模式，这就是为什么对不同的中文编码格式不对出现乱中文的原因

print('王忠全'.encode('gbk').decode('gbk'))    # 编码解码格式必须相同

# 列表[] 元组() 字典{} 集合{}    * 重要 !!!!

# 列表-list-[] 可变有序
# 元组-tuple-() 不可变有序
# 字典-dict-{} 可变无序
# 集合-set-{}  可变无序

x_list = [1, 2, 3]    # 下标从0开始，和C语言的数组一样
x_tuple = (1, 2, 3)   # 下标从0开始，和C语言的数组一样   注意元组只有一个元素的时候要加,号 (3,)
x_dict = {'a': 97, 'b': 98, 'c': 100}
x_set = {1, 2, 3}

# 访问数据
print(x_list[1])
print(x_tuple[1])
print(x_dict['a'])
print(3 in x_set)

y_list = [1, 2, 3]
print(x_list + y_list)  # 列表与列表之间可以相加

print([1, 2, 3] * 3)    # 列表翻倍
print('abc' * 3)

print(3 / 2)    # 除
print(15//4)    # 整除
print(15.0//4)  # 前面是小数的整除
print(-15//4)   # 向下取整

# %c - 字符 %d - 整数
# %f - 实数 %s - 字符串

print('%c' % (65,))

# 惰性求值

# 成员测试运算符in  同一性测试运算符is

print(3 in [1, 2, 3])

x = []
for i in range(1, 10):
    x.append(1)
    print(i)
    print(x)

print('abc' in 'akibhgcabc')

for i in (3, 5, 7):
    print(i)

# is 同一性测试运算符 如果两个对象是同一个，两者具有相同的地址

print(3 is 3)
x = [300, 300, 300, 300]  # 基于值的内存管理，同一个值在内存中只有一份
print(x[0] is x[2])       # TRUE

print([1, 2, 3] is [1, 2, 3])  # 列表在不同的指针，表头不一样，但是列表里面存储的值，其实是对象的地址（列表存的是指针）

x.append(4)               # append()列表新增
print(x)

x = [1, 2, 3]
x = y             # 让他们都指向同一个地址
print(x is y)

# 逻辑运算符 and or not

# Python并不支持++或者是--运算

# Python关键字

# Python的内置函数
# print(dir(__builtins__))

# 类型转换 bin() oct() hex()

print(bin(555))    # 转换为二进制函数bin
print(oct(555))    # 转换为八进制函数oct
print(hex(555))    # 转换为十六进制函数hex

# 编码函数
print(ord('a'))    # 用来查看指定字符的Unicode编码
print(chr(65))     # 返回数字为65的对应字符
print(ord('王'))

print(type(str([1, 2, 3])))   # str强制转换为字符类型
ascii('a')
bytes('王忠全', 'utf-8')

# 强制转换元素类型
# list() tuple() dict() set()

a = [1, 2, 3]
b = ['a', 'b', 'c']
print(zip(a, b))    # zip 返回的是一个对象，需要手动将其list()列表化,或者dict()字典化
print(list(zip(a, b)))
print(dict(zip(a, b)))

print(frozenset('12345'))    # 冻结集合，元素不可改变

# 判断类型
print(isinstance(3, int))

# max()最大函数 min()最小函数 sum()求和函数 len()判断长度函数

# print(sum([[1, 2], [3], [4]], []))

# 列表推导式 2**i for i in range(200)

# x = input("请输入一个数字：")
# print('您输入的是：', x)
# print(type(x))

x = eval("[1, 2, 3]")
print(x)
print(type(x))

x = list(range(11))
print(x)
import random
random.shuffle(x)    # 打乱列表
print(x)

print(sorted(x))

print(list(reversed(x)))    # 逆序

print(list(map(str, range(5))))    # map函数返回的可迭代对象

# 用map实现双函数映射，列表相加


def add(x, y):
    return x + y


n = list(map(add, range(5), range(5, 10)))    # 我们可以使用list和map函数来将add函数应用到两个列表上，其中第一个列表是从0到4，第二个列表是从5到9
print(n)

n = list(map(lambda x,y: x+y, range(5), range(5, 10)))    # 使用匿名函数lambda
print(n)


def myMap(iterable, op, value):
    if op not in '+-*/':
        return '错误输出'
    func = lambda i : eval(repr(i) + op + repr(value))    # 自定义函数实现四则运算
    return map(func, iterable)


print(list(myMap(range(5), '+', 5)))

x = random.randint(1, 1e30)    # 随机生成一个指定范围的随机整数
print(x)

print(list(map(int, str(x))))   # 将x变成字符串，之后映射到int函数，变成数字


import operator
print(operator.add(3, 5))


def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7])
print(list(newlist))

# range()函数   range(start, stop, step) 开始，结束，步长   左闭右开 -- [开始，结束)


# 课后习题

print(int('11111', 2))
print(chr(ord('D') + 2))








