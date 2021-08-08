def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a, a)
def findgcd(array,n):
    res = array[0]
    for i in range(1,n):
        res = gcd(array[i],res)
    return res
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    maxi = max(a)
    p = findgcd(a,n)
    mini = min(a)
    for i in range(n):
        if a[i]==maxi:
            a[i]=p
            break
    res=0
    for i in range(n):
        res = res+a[i]//p
    print(res)
        
