for _ in range(int(input())):
    n,a,b=map(int,input().split())
    str = "EQUINOX"
    c=0
    d=0
    for i in range(n):
        x=input()
        if x[0] in str:
            c+=a
        else:
            d+=b
    if c>d:
        print("SARTHAK")
    elif d>c:
        print("Anuradha")
    else:
        print("Draw")
