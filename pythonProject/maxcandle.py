n=int(input())
li = list(map(int,input().split(' ')))
x=max(li)
c=0
for i in li:
    if i==x:
        c+=1
print(c)