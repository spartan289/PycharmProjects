s, t=map(int,input().split())
a, b=map(int,input().split())
m, n=map(int,input().split())
app=list(map(int,input().split()))
ora=list(map(int,input().split()))
c=0
d=0
for i in app:
    if i+a in range(s,t+1):
        c+=1
for i in ora:
    if i+b in range(s,t+1):
        d+=1
print(c)
print(d)