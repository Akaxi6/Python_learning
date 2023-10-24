# 第六章 面向对象的程序设计 （Object Oriented Programming）OOP

# 面向对象的关键就是如何定义这些类并且组织这些类的关系  （对象[实例] -- 类）

# Python是面向对象的解释型高级动态语言

# 数据成员 -- 成员方法

# 6.1 【类的定义与使用】

class Car(object):         # 定义一个类，继承与object
    def infor(self):       # 定义成员方法
        print('这是一个车')

# 实例化对象
my_car = Car()
my_car.infor()    # 通过 对象名.成员 可以访问其中的数据成员或成员方法

print(isinstance(my_car, Car))    # 判断对象类型

# 对象的数据成员 / 类的数据成员

# 类的数据成员


class Demo(object):
    total = 0

    def __new__(cls, *args, **kwargs):    # * 可变参数    cls: 数据成员
        if cls.total >= 3:
            raise Exception('最多为3')
        else:
            return object.__new__(cls)

    def __init__(self):     # 自动调用函数
        Demo.total = Demo.total + 1

# 对象的数据成员
class A:
    def __init__(self, value1 = 0, value2 = 0):    # 默认值value1\2   【init函数初始化 】
        self.value1 = value1
        self.value2 = value2


a = A()  # 实例化
print(a.value1)
# print(A.value1)

a2 = A(10, 12)
print(a2.value1)


# 私有成员 / 共有成员 / 受保护成员

# _xxx:  受保护成员
# __xxx: 私有成员（子类不能访问）
# __xx__ 系统定特殊成员

# self 参数代表当前对象

class Root:
    __total = 0

    def __init__(self, v):    # 构造方法
        self.__value = v      # value属于对象
        Root.__total += 1     # total属于类

    def show(self):           # 共有方法
        print('s', self.__value)
        print('t', Root.__total)

    def __pr_show(self):      # 私有方法
        print('s', self.__value)
        print('t', Root.__total)


root = Root(100)

root.show()    # 对象名调用
Root.show(root)    # 类调用


# 类方法

class Root:
    __total = 0

    def __init__(self, v):    # 构造方法
        self.__value = v      # value属于对象
        Root.__total += 1     # total属于类

    def show(self):           # 共有方法
        print('s', self.__value)
        print('t', Root.__total)

    @classmethod    # 类方法
    def classshow(cls):
        print(cls.__total)

    @staticmethod    # 静态方法
    def staticshow():
        print(Root.__total)

# 抽象方法

import abc

class Foo(metaclass=abc.ABCMeta):    # 抽象类
    def f1(self):
        print(123)

    def f2(self):
        print(456)

    @abc.abstractmethod
    def f3(self):
        print(789)


# 属性
'''
class Test:
    def __init__(self, value):
        self.__value = value
'''

# 混入机制
class Car:
    price = 10000
    def __init__(self, c):
        self.color = c

car1 = Car("Red")
car2 = Car("Blue")
print(car1.color, car1.price)

# 封装、继承、多态

# 6.3 继承
# 内置函数super()

# 多态

# 6.4 特殊方法、运算符重载

# __init__构造函数
# __del__ 析构函数






