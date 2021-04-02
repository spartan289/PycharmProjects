def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
count=0
l,r=map(int,input().split())
for j in range(min(l,r)):
    for i in range(l,r+1):
        if(gcd(j,i)==1):
            print(j)
            
