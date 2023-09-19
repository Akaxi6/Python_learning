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

