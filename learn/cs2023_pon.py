
for _ in range(int(input())):
    n,b = map(int,input().split())
    a = list(map(int,input().split()))
    cur=-1
    for i in a:
        if i&b==b:
            cur&=i
    if cur==b:
        print("Yes")
    else:
        print("No")