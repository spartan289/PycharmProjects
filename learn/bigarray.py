for _ in range(int(input())):
    n,s=map(int,input().split())
    su=(n*(n+1))//2
    if(su>s):
        if((su-s)<=n):
            print(su-s)
        else:
            print(-1)
    else:
        print(-1)
# for _ in range(int(input())):
#     n,s = map(int,input().split())
#     if n>=s:
#         print(s)
#     else:
# #         print(n-(s-n))
# for _ in range(int(input())):
#     n = int(input())
#     n = n%4
#     if n==0:
#         print("North")
#     elif n==1:
#         print("East")
#     elif n==2:
#         print("South")
#     else:
# #         print("West")
# for _ in range(int(input())):
#     n= int(input())
#     if n==2:
#         print(-1,-1)
#         print(-1,-1)
#     else:
#         for i in range(n):
#             for j in range(n):
#                 if i==j:
#                     print(-1,end=" ")
#                 else:
#                     print(1, end=" ")
#
#             print()
