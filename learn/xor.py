def pow(a,b):
    mod=1e9
    if b==0: return 1
    if b==1: return a
    if b%2==0 :
        t=pow(a,(b-1)//2)
        return t*t%mod
    else:
        t=pow(a,(b-1)//2)
        return (((a*t) % mod) * t) % mod

for _ in range(int(input())):
    c=0
    n=int(input())
    n=2**n
    mod=1e9

    n=int(n % (1000000000 + 7))
    for i in range(n):
        if i^(i+1)==(i+2)^(i+3):
            c+=1
    print(c)