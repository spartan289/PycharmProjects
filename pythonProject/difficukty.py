t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    k=int(input())
    l.reverse()
    for i in range(len(l)):
        if k>=l[i]:
            k = (k-l[i])
            l[i]=0


    for i in range(10):
        if l[i]!=0:
            print(10-i)
            break