n= int(input())
str=[]
query=[]
for y in range(n):
    x=input()
    str.append(x)
m=int(input())
for z in range(m):
    x=input()
    query.append(x)
li=[]
i=0
while i <m:
    c=0
    j=0
    while j<n:
        if query[i] == str[j]:
            c += 1
        j += 1
    li.append(c)
    i += 1
print(list(li))