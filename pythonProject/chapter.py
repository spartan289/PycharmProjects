t=int(input())
for _ in range(t):
    x,m,k=map(int,input().split())
    li=list(map(int,input().split(' ')))
    sum=0
    for i in li:
        sum+=i
    d=sum//m
    if d<=k:
        print(d)
    else:
        print(k)