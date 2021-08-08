for _ in range(int(input())):
    d,x,y,z = map(int,input().split())
    f1 = x*7
    f2 = d*y+(7-d)*z
    print(max(f1,f2))
