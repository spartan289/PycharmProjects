import bisect
def numsquares(n)->int:
    perfectsquares = [i*i for i in range(100,0,-1)]
    for i in perfectsquares:
        if n%i==0 or n%i!=n:pass