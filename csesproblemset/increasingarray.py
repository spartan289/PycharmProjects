n=int(input())
li = list(map(int,input().split()))
c=0
for i in range(n):
    x = li[i]
    res = li[i]
    for j in range(i, n):
        res = min(res, li[j])
    res = li.index(res)
    li[i],li[li.index(res)] = li[res],li[i]
    c+=1
    if sorted(li):
        break


