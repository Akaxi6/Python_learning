# Python序列结构



# 3.3.2 字典元素的访问

# 3.3.3 元素的添加、删除、修改

aDict= {'age': 37, 'score': [98, 97], 'name': 'Dong'}
print(aDict.popitem())   # 随机弹出，如果指定使用remove\discard

# Counter类也可以用来统计

# 3.4 集合set{}

# 无序可变序列，大括号作为界定符，里面的数字没有重复

a = {3, 5} # 创建集合
print(type(a))

s = {1, 2, 3}
s.add(3)
print(s)

# s.remove(5) 不存在就会报错

# 集合的运算，交、并、补、包含<、>、==

# 应用案例，去重好用

# 3.5 序列解包

x, y, z = 1, 2, 3
x, y, z = range(3)  # 序列解包个数必须一一对应
print(x)
print(y)
print(z)
# x, y, z = range(4)  # 比如这个就会报错

