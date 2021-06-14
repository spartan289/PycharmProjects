n,q=map(int,input().split())
li=[0]*n
max=0
for j in range(q):
    a,b,k=map(int,input().split())
    for i in range(a-1,b):
        li[i]+=k
print(max)

