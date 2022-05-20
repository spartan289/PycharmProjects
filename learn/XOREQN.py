# def xoreqn(n,arr):
#     for x in range(10**5):
#         pro = arr[0]+x
#         for i in range(1,n):
#             pro=pro^(arr[i]+x)
#         if pro==0:
#             print(x)
#             break
# xoreqn(5,[2,4,5,6,7])

def makepal(arr,n):
    odd=0
    total = 0
    for i in range(n):
        if arr[i]%2!=0:
            odd+=1
    if odd>1:
        total = odd//2
    print(total)
for _ in range(int(input())):
    n=int(input())
    arr = list(map(int, input().split()))
    makepal(arr, n)

def HILLSEQ(arr,n):
    map = {}
    for i in arr:
        if i in map:
            if map[i]==2:
                return -1
            else:
                map[i]+=1
        else:
            map[i]=1
