t=int(input())
for _ in range(t):
    n,e,h,a,b,c=map(int,input().split())
    li=[]
    for x in range(e):
        for y in range(h):
            f=2*a*x + 3*b*y+c*(e+h)-c*(x+y)
            li.append(f)
    print(max(li))