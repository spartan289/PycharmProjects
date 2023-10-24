for _ in range(int(input())):
    a,b = map(int,input().split())
    x = (2*a-b)
    y = (2*b-a)
    if x%3==0 and y%3==0 and x>=0 and y>=0:
        print("YES")
    else:
        print("NO")



