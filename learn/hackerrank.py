n,c=map(int,input().split())
li=list(map(int,input().split()))
c=[]
for i in li:
    for j in range(n):
        c.append(abs(i-j))
print(max(c))
