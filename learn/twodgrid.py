n=int(input())
x=[]
y=[]
for _ in range(n):
    a,b=map(int,input().split())
    x.append(b)
    y.append(a)
r=max(y)
c=max(x)
zeros = [ [0]*r for _ in range(c) ]
print(list(zeros))
for i in range(n,)