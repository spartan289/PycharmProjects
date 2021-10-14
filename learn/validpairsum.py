from bisect import *
def validpair(a,n):
    c=0
    a.sort()
    for i in range(n):
        if a[i]>0:
            j = bisect_left(a,-a[i]+1)
            c+=i-j
    return c

print(validpair([-1,-1,-1,0],3))