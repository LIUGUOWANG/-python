# 编写人：刘富贵 
# 日期：2025-01-26 时间：11:05

#遍历字符串
for i in 'hello':
    print(i)

#range()函数，Python中的内置函数，产生一个[n,m)的整数序列
for i in range(1,11):
    #print(i)
    if i%2==0:
        print(i,'是偶数')

print('--------------找出100-999中水仙花数-------------')
for i in range(100,1000):
    a=i%10
    b=i//10%10
    c=i//100
    if a**3+b**3+c**3==i:
        print(i)

#遍历for 循环的扩展形式
a=0
for i in range(1,11):
    a+=i
else:
    print(a)