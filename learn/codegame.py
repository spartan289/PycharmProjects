# for _ in range(int(input())):
#     n= int(input())
#     if(n==1 or n==2):
#         print(0)
#
#     elif(n%2==0):
#         print(n//2-1)
#     else:
#         print(n//2)
for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    h.sort()
    i=0
    j=n-1
    ans=0
    while(i<j):
        if(h[i]+h[j]<=n):
            ans+=1
            i+=1
            j-=1
        else:
            j-=1
    print(ans)