a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    for j in b:
        if i==j:
            if i not in c:
                c.append(i)
print(list(c))