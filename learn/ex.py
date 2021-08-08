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
for q in range(int(input())):
    l,r = map(int,input().split())
    p=1
    x = 1
    for i in range(l+1,r+1):
        x = x*(oddlength(str(l))**oddlength(str(i)))
        p = p*power(oddlength(str(l)),oddlength(str(i)),10**9+7)
    p=p%(10**9+7)
    print(p)
