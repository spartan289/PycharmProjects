def seive(n):
    prime = [True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    return prime
n = int(input())
prime = seive(n)


if n in [1,2,3,4]:
    print(0)

else:
    c=0
    for l in range(2,n):
        if prime[l]:
            for r in range(l+1,n):
                if l+r>n:
                    break
                if prime[r]:
                    if prime[l+r] and l+r<=n:
                        c+=1
    print(c)


