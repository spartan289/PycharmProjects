def power(x, y, p):
    res = 1

    x = x % p

    if (x == 0):
        return 0

    while (y > 0):

        if ((y & 1) == 1):
            res = (res * x) % p

        y = y >> 1
        x = (x * x) % p
    return res
def oddlength(n):
    res=n
    for j in range(len(n)-2,-1,-1):
        res+=n[j]
    return int(res)
arr = [0]*(10**5+1)
arrsm = [0]*(10**5+1)
for i in range(1,10**5+1):
    arr[i] = oddlength(str(i))
    arrsm[i] = arrsm[i-1]+arr[i]
for q in range(int(input())):
    l,r = map(int,input().split())
    pow = arrsm[r]-arrsm[l]
    p = power(arr[l],pow,10**9+7)  

    print(p)