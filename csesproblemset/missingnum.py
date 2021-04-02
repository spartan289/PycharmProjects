n=int(input())
li=list(map(int,input().split()))
li.sort()
for i in range(n):
    if li[i]!=i+1:
        print(i+1)
        break
