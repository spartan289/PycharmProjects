li=list(map(int,input().split(' ')))
x=sum(li)
l=[]
for i in li:
    l.append(x-i)
print("{} {}".format(min(l),max(l)))