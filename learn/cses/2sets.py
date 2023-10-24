n = int(input())
x = n*(n+1)//2
if x%2!=0:
    print("NO")
else:
    print("YES")
    y = x//2
    s1 = []
    s2 = []
    for i in range(n,0,-1):
        if i<=y:
            s1.append(i)
            y=y-i
        else:
            s2.append(i)
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)
