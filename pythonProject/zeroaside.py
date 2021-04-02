n=int(input())
li=list(map(int,input().split()))
c=0
for i in range(n):
    if li[i] != 0:
        print(li[i],end=" ")
    else:
        c+=1
for i in range(c):
    print(0,end=" ")
