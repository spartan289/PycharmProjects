n, k = map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in n:
    for j in (i+1,n):
        if (arr[i]+arr[j])%k==0:
            c+=1
print(c)
