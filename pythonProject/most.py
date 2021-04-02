n=int(input())
l=list(map(int,input().split()))
l.sort()
res=l[0]
max_count=1
cur_count=1
for i in range(1,n):
    if l[i]==l[i-1]:
        cur_count+=1
    else:
        if cur_count > max_count:
            max_count=cur_count
            res=l[i-1]
        cur_count=1
if cur_count > max_count:
    max_count=cur_count
    res=l[n-1]
print(res)

