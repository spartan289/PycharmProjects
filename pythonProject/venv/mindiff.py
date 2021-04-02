t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    mindiff=10000000
    for i in range(0,n-1):
        mindiff=min(mindiff,arr[i+1]-arr[i])
    for i in range(0,n-1):
        if arr[i+1]-arr[i]==mindiff:
            a=arr[i]
            b=arr[i+1]
    if a < b:
        print("{} {}".format(a,b))
    else:
        print("{} {}".format(b,a))

        
