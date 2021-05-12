
for _ in range(int(input())):
    m,s=map(int,input().split())
    c=0
    while(m>=s):
        m=m-s
        c+=1
    print(c)

