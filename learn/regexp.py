import math
def solve(n,k):
    a=1
    b=-n
    c=n*k
    d=b*b-4*a*c
    if d<=0:
        return n-1
    exlower =  int(math.floor(-b-math.sqrt(d))/(2*a))
    while isTooFar(a,b,d,exlower):
        exlower+=1
    exupper =  int(math.ceil(-b+math.sqrt(d))/(2*a))
    while isTooFar(a,b,d,exupper):
        exupper-=1
    return (n-1) - (exupper-exlower+1)
def isTooFar(a,b,d,x):
    return math.pow(x*2*a+b,2)>=d
for _ in range(int(input())):
    n,k=map(int, input().split())
    print(solve(n,k))
    