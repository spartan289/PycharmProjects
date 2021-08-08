for _ in range(int(input())):
    a,b,c,d = (map(int,input().split()))
    if (a==b and b==c and d==c and a==c and a==d and b==d):
        print(0)
    elif ((a!=b and b!=c and c!=d and a!=c and a!=d and b!=d) or (c==d) or (a==d) or (a==b) or (b==d) or (c==b) or (a==c)):
        print(2)
    elif ((a!=b and b==c and c==d) or (a!=b and a==c and c==d) or (b!=c and a==c and c==d ) or (b!=c and a==b and b==d) or (c!=d and a==b and b==c) or (c!=d and a==b and b==d) or (a!=d and b==c and c==d) or (a!=d and a==b and b==c) or (d!=b and a==c and c==d ) or (d!=b and a==b and b==c)):
        print(1)

