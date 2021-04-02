a,x,y,z=map(int,input().split())
lx=list(map(int,input().split()))
ly=list(map(int,input().split()))
lz=list(map(int,input().split()))
b=[]
for i in lx:
    for j in ly:
        for k in lz:
            if (i+j+k)<a:
                x=a-(i+j+k)
                b.append(x)
            
if len(b)==0:
    print(-1)
print(min(b))