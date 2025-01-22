# 编写人：刘富贵 
# 日期：2025-01-17 时间：19:43
with open('text.txt','r') as fp:
    content=fp.read()
    print(content)

fp=open('text.txt','r')
content=fp.read()
print(content)

with open('text.txt','w') as fp:
    print('content',file=fp)

