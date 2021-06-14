n,d=map(int,input().split())
arr=list(map(int,input().split()))
x=n-d
for i in range(d,n):
    print(arr[i],end=" ")
for i in range(d):
    print(arr[i],end=" ")
