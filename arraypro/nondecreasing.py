from math import ceil
def nondecresing(arr,n):
    b = [0]*n
    b[0]=arr[0]
    for i in range(1,n):
        if arr[i]<b[i-1]:
            b[i]=arr[i]*ceil(b[i-1]/arr[i])
        if arr[i]>=b[i-1]:
            b[i] = arr[i]
    return b
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    b = nondecresing(arr,n)
    for i in b:
        print(i,end=" ")
    print()
