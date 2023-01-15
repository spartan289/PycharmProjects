def minnoofgift(n,g,arr: list):
    arr.sort()
    sum=0
    for i in range(n):
        sum+=arr[i]
    return sum
for _ in range(int(input())):
    n = int(input())
    g = int(input())
    arr = list(map(int,input().split()))
    sum = minnoofgift(n,g,arr)
    print(sum)