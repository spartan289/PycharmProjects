for _ in range(int(input())):
    n,p,k = map(int,input().split())
    np = [i%k for i in range(n)]
    c=0
    print(np)
