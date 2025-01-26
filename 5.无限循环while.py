# 编写人：刘富贵 
# 日期：2025-01-26 时间：12:01

answer=input('今天上课吗？y/n')#初始化变量
while answer=='y':#条件判断
    print('好好学习，天天向上')#语句块
    answer = input('今天上课吗？y/n')#改变变量

a=0
i=1
while i<=100:
    a+=i
    i+=1
print(a)

#扩展形式
a=0
i=1
while i<=100:
    a+=i
    i+=1
else:
    print(a)
