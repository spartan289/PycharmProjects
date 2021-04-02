def avg(li):
    n=len(li)
    x=sum(li)

    return x/n

li=list(map(int,input().split()))
x=avg(li)
print('%.2f'%x)