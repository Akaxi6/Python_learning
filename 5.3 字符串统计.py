# 编写函数，接收一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，并以元组的形式返回结果

def sumchar(s):
    '''
    函数作用：分别统计大写字母、小写字母、数字、其他字符的个数
    输入：字符串s
    返回：统计个数的元组result
    '''
    result = [0, 0, 0, 0]
    for chr in s:
        if chr.isupper():    # 大写字母
            result[0]+= 1
        elif chr.islower():  # 小写字母
            result[1]+= 1
        elif chr.isdigit():  # 数字
            result[2]+= 1
        else:                # 其他
            result[3]+= 1

    return tuple(result)


x = input("请输入一个字符串：")
y = sumchar(x)    # y里面为分别统计的个数
print("大写字母个数：{0}，小写字母个数：{1}，数字个数{2}，其他字符个数{3}".format(y[0], y[1], y[2], y[3]))    # 输出统计量


def sumchar_ASCII(s2):
    '''
    函数作用：分别统计大写字母、小写字母、数字、其他字符的个数
    输入：字符串s
    返回：统计个数的元组result
    '''
    result2 = [0, 0, 0, 0]
    for chr2 in s2:
        if  65 <= ord(chr2) <= 90:   # 大写字母
            result2[0]+= 1
        elif 97 <= ord(chr2) <= 122:  # 小写字母
            result2[1]+= 1
        elif 48 <= ord(chr2) <= 157:  # 数字
            result2[2]+= 1
        else:                # 其他
            result2[3]+= 1

    return tuple(result2)

x2 = input("请输入一个字符串：")
y2 = sumchar(x2)    # y里面为分别统计的个数
print("大写字母个数：{0}，小写字母个数：{1}，数字个数{2}，其他字符个数{3}".format(y2[0], y2[1], y2[2], y2[3]))    # 输出统计量


