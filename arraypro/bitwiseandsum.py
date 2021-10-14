def bitwiseand(arr,n):
    sum = arr[0]
    for i in range(1,n):
        sum = arr[i] & sum
    return sum

def f(i,j,arr):
    ar = arr[0:i]+arr[j+1:len(arr)]
    return bitwiseand(ar,len(ar))
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    su = 0
    for i in range(n):
        for j in range(i,n):
            if i==0 and j==n-1:
                continue
            x = arr
            su = su+f(i,j,x)
    print(su)
