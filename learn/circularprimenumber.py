def sieve(n):
    prime = [True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    return prime
def isCircularPrime(n):
    prime = sieve(10**5)
    n=[int(i) for i in str(n)]
    for i in range(len(n)):
        temp = n.pop(0)
        n.append(temp)
        x = map(str, n)
        x = ''.join(x)
        x = int(x)
        if not prime[x]:
            return False
    return True
print(isCircularPrime(110))