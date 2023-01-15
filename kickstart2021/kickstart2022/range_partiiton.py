def partition(n,x,y):
    sum = n*(n+1)//2
    sum = sum*x

    if(sum%(x+y)==0):
        return paritiion(n,sum//(x+y))
    else:
        return -1
def paritiion(N,partitionsum):
    if(partitionsum==0 or N==0):
        return []
    if(N>partitionsum):
        return paritiion(N-1,partitionsum)
    else:
        return [N]+paritiion(N-1,partitionsum-N)
for _ in range(int(input())):
    n,x,y = map(int,input().split())
    ans = partition(n,x,y)
    if(ans==-1):
        print("Case #{}: IMPOSSIBLE".format(_+1))
    else:
        print("Case #{}: {}".format(_+1,"POSSIBLE"))
        print(len(ans))
        print(*ans)

