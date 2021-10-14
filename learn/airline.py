for _ in range(int(input())):
    a,b,c,d,e = map(int,input().split())
    if a<=e and b+c<=d:
        print("YES")
    elif b<=e and a+c<=d:
        print("YES")
    elif c<=e and a+b<=d:
        print("YES")
    else:
        print("NO")
