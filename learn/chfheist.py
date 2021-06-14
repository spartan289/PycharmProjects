for _ in range(int(input())):
    D,d,p,q = map(int,input().split())
    n=D//d
    totalMoney = D*p
    total = int((d*(n)*(n-1))//2)+int(n*(D%d))
    print(totalMoney+q*total)

