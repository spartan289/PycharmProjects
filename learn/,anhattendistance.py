def manhattendistanc(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
def sumoofdistance(arr,n):
    if n==1:
        return 0
    alternatedist = []
    for i in range(1,n):
        alternatedist.append(manhattendistanc(arr[i-1],arr[i]))
    print(alternatedist)
    print(sum(alternatedist))
for _ in range(int(input())):
    n = int(input())
    li = []
    for i in range(n):
        a = list(map(int,input().split()))
        li.append(a)
    sumoofdistance(li,n)
def sumPairs(arr,n):
    sum=0
    for i in range(n):
          sum+= arr[i]*(2*n)



