for _ in range(int(input())):
    D,d,a,b,c = map(int,input().split())
    d=d*D
    x=0
    if d>=42:
        x+=c
    elif d>=21:
        x+=b
    elif d>=10:
        x+=a
    print(x)