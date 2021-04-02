n,h,x = map(int,input().split())
l=list(map(int,input().split(' ')))
c=0
for i in l:
    if i+x==h:
        c+=1
if c>0:
    print("YES")
else:
    print("NO")