t=int(input())
for _ in range(t):
    p = int(input())
    li = list(map(int,input().split(' ')))
    li.pop(0)
    c=0
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            c+=1
            if i==j:
                c+=1
    print(c)
