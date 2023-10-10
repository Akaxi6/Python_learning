# 第七章 字符串

# 字符串是不可变有序序列

# isinstance
# u'你好' -- u表示Unicode编码格式   字节串

# 7.1 字符串编码格式简介
# gbk2312 / gbk / utf-8 / unicode
# 字符串编码有加密的效果

# 7.2 转义字符串与原始字符串

print('\102')   # 三位八进制
print('Hello\nworld!')  # 换行\n

print(r'\n\n')  # 加一个r表示字符串里面的都不转义
print('\\n\\n') # 两个\不转义

# 7.3 格式化 % {}

x = 1235
# % [(name)] [flags] [width] . [precision] typedecode % 表达式
# %s %r %c %d

so = "%o" % x
print(so)

# format{}

print('{0:.3f}'.format(1/3))

name = 'Akaxi'
age = 28
print(f'Myname is {name},and I am {age} years old')

# 字符串不可变、但是可以切片

# 7.4 find()查找函数 rfind()查找函数 index()函数 rindex()函数 counts()函数
s = 'apple,peach,pear,peach'
print(s.find('peach'))
print(s.find('peach', 7, 25))

print(s.count('p'))

# split()分割函数、rsplit()函数、partition()函数、rpartition()函数

print(s.split(','))
print(s.partition(','))

s2 = 'Hello My \n world is good!'
print(s2.split())

print('a,,,bb,,ccc'.split(','))    # 每个都好都被看作独立的分隔符，两个逗号之间的空格也被分割出来 -- 两个逗号中间有“空串”
s3 = 'a,,,bb,,ccc'
print(s3.split(','))

# 字符串链接join()
li = ['wzq', 'big', 'handsome,boy']
x = ' '.join(li)
print(x)

s4 = '你好中国，我爱中国'
print(s4)

s5 = s4.replace('中国', '家国')
print(s5)

# replace()替换函数、maketrans()字符映射表、translate()函数
table = ' '.maketrans('abcdefg', '1234567')
s6 = 'alkhbdssbcdfes'
print(s6.translate(table))

# 凯撒加密，每个字母替换为后面第k个
import string
def kaisa(s, k):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    # 创建映射表


# 删除指定字符strip()

# s.startswith(s) 是否指定字符开始、s.endswith(s) 是否指定字符结束    重要！！！！！！！！

# isalnum()

y2 = 'Hello world!'.center(20)
print(y2)

y3 = 'Hello world!'.rjust(20)
print(y3)


# 7.4 字符串支持运算

print(eval('3+4+5'))

path = r'C\\python\\test.bmp'
new_path = path[:-4] + '_new_' + path[-4:]
print(new_path)

# 7.6 中文字符串jieba库


# 案例欣赏











