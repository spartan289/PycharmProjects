def mod(m,a):
    if m<a:
        return m
    else:
        return m%a
for _ in range(int(input())):
    n,m=map(int,input().split())
    c=0
    x=0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            x+=1
            if i*j>n**2:
                break

            if mod(mod(m,i),j) == mod(mod(m,j),i):
                c += 1
    print(c)

