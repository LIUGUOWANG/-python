# 编写人：刘富贵 
# 日期：2025-01-26 时间：12:45

i=0
while i<3:
    username=input('请输入用户名：')
    pwd=input('请输入密码：')
    if username=='lfg' and pwd=='123456':
        print('正在登录...')
        i=5
    else:
        if i<2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
        else:
            print('请一分钟后再试')
    i+=1

