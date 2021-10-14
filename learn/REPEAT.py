for _ in range(int(input())):
    n,k,s = map(int,input().split())
    upper = s-n*n
    print(upper//(k-1))