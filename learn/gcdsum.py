def findGCDSum(n, a):
    gcdsum=0
    tempgcd=0
    for i in range(n-1):
        gcdsum+=gcd(a[i],a[i+1])
    return gcdsum
def gcd(a,b):
    return a if(b==0) else gcd(b,a%b)
for _ in range(int(input())):
    k=int(input())
    for j in range(1,k+1):
        a=[(j+i**2) for i in range(1,2*j+2)]
        print(findGCDSum(len(a),a))

