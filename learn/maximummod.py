def maximum(arr,n):
    ans = 0
    for i in range(n):
        ans+=arr[i]-1
    return ans
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(maximum(arr,n))