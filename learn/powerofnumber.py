def power(n,x):
    assert n>=1 and x>=0 and int(x)==x and int(n)==n,'The number should be a positive integer greater than 1'
    if x==0:
        return 1
    if x==1:
        return n
    return n*power(n,x-1)
print(power(0,0))