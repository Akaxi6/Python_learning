# 第四章 程序控制结构

# 4.1 条件表达式

# 关系运算符
print(1 < 2 < 3)
print(1 < 2 > 3)
print(1 < 3 > 2)

# 4.2 选择结构 if

jitui, tu = map(int, input('输入总数(中间空格)').split())  # map映射成数字
tu = (tu - jitui*2)/2
if int(tu) == tu:
    print('鸡:{0},兔:{1}'.format(in t(jitui-tu),int(tu)))
else:
    print('错误')

# 循环结构 for while
s = 0
for i in range(1, 101):
    s+= i
else:
    print(s)

for i in range(1, 101):
    if i %7 ==0:
        print(i)

# 打印九九乘法表
'''for i in range(1, 10):
    for j in range(1, i+1):
    print('{0}')'''

# break 、continue
# 判断最大的素数，除1以外没有其他因数
for n in range(100, 1, -1):               # 从100每次减1
    if n % 2 == 0:                        # 如果这个数字除以2没有余数，说明他能被因式分解
        continue                          # 结束本次循环，他不是素数
    for i in range(3, int(n**0.5)+1, 2):  # 不能被2整除，找他的因式分解
        if n % i == 0:                    # 如果能被因式分解
            break                         # 结束
    else:                                 # 都不能被因式分解，则他是素数
        print('这个最大的素数是：', n)
        break

# 4.4 案例

# 判断天数
import time

date = time.localtime()
year, month, day = date[:3]
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):
    day_month = 29
if month == 1:
    print(day)
else:
    print('这是今年的天数：',sum(day_month[:month-1])+day)

# 成绩计算

while True:
    try:
        n = int(input('输入评委的人数：'))
        if n <= 2:
            print('评委人数少于两个')
        else:
            break

    except:
        pass

scores = []  # 创建一个存储评委分数的列表

for i in range(n):
    while True:
        try:
            score = input('请输入第{0}个评委的分数：'.format(i+1))
            score = float(score)
            assert 0 <= score <= 100  # 假设分数在这个区间，正确就继续运行，错误就会跳出到except
            scores.append(score)      # 把分数添加进去
            break
        except:  # 分数不在0-100的区间内错误
            print('分数错误')

highest = max(scores)
lowest = min(scores)
scores.remove(highest)
scores.remove(lowest)
final = round(sum(scores)/len(scores), 2)
print('去掉一个最高分{0}分，去掉一个最低分{1}分，最终成绩是：{2}分！'.format(highest, lowest, final))
