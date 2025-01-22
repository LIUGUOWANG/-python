# 编写人：刘富贵 
# 日期：2025-01-22 时间：17:09
#顺序结构
print('-'*40)
# 赋值运算的顺序是从右到左
a=b=c=d=10
print(a)
print(b)
print(c)
print(d)


print('-'*40)
#选择结构1：单分支结构
number=eval(input('请输入6位中奖号码：'))
if number==147258:
    print('恭喜中奖！')
if number!=147258:
    print('未中奖')

print('-'*40)
#0布尔值为False，其他为Ture
#空字符串的布尔值为False，其他为Ture

#选择结构2：双分支结构

number=eval(input('请输入6位中奖号码：'))
if number==147258:
    print('恭喜中奖！')
else:
    print('未中奖')

print('——————以上代码可以使用条件表达式简化——————')

result='恭喜中奖！' if number==147258 else '未中奖'
print(result)

#选择结构2：多分支结构
score=eval(input('请输入成绩：'))
if score<0:
    print('成绩有误')
elif 0<=score<60:
    print('不及格')
elif 60<=score<80:
    print('合格')
else:
    print('优秀')