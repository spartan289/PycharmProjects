import math


def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
for _ in range(int(input())):
    n=int(input())
    n=math.sqrt(n)
    li = list(primes_sieve1(n))
    z=0
    for p in range(1,len(li)):
        x = li[p - 1] * li[p]
        if p != 0 and (x < n or x==n):
            z=x
        else:
            break
    print("Case #{}: {}".format(_+1,z))