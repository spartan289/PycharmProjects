t=int(input())
for _ in range(t):
    n,b=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    sum=0
    c=0
    for i in range(n):
        sum+=li[i]
        if sum>b:
            break
        c+=1
    print("Case #{}: {}".format(_+1,c))
