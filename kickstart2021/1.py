t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    l=0
    r=n-1
    c=0
    while l<r:
        c+=s[l]!=s[r]
        l+=1
        r-=1
    print("Case #{}: {}".format(_+1,abs(k-c)))





