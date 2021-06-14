Integermaxvalue = 100000

for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = [997 for i in range(n)]
    left=-1
    right = -1
    max = Integermaxvalue
    for i in range(n):
        if i==0:
            ans[i]=0
        elif a[i]!=0:
            ans[i]=0
        else:
            ans[i] =max


    for i in range(n):
        if ans[i]==1:
            right = i
        if right!=-1:
            if ans[i]!=0:
                ans[i] = min(ans[i],i-right)

    for i in range(n-1,-1,-1):
        if ans[i]==2: left = i
        if left!=-1:
            if ans[i]!=0 : ans[i] = min(ans[i],left-i)
    for i in range(m):
        j = b[i]-1
        if ans[j]!=max:
            print(ans[j],end=" ")
        else:
            print(-1,end=" ")
    print()


