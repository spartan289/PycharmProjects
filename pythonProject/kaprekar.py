p=int(input())
q=int(input())
if p<2:
    print(1,end=" ")
for i in range(p,q):

    s=str(i**2)
    if len(s)%2==0:
        n=len(s)
        a=s[0:n//2]
        b=s[n//2:n]
        if int(a)+int(b)==i:
            print(i,end=" ")
    if len(s)==10:
        n=len(s)
        c=s[0:n//2-1]
        d=s[n//2-1:n-1]
        if int(c)+int(d)==i:
            print(i,end=" ")