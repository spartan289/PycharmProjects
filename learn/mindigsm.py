def f(n,b):
    result=0
    while(n>0):
        remainder = n%b
        result += remainder
        n = n//b
    return result

# def printf(n,l,r):
#     current=1000000000000
#     p=-1
#     if n<l:
#         return n
#     else:
#         if n<l and n>r:
#             for b in range(n,r+1):
#                 x = f(n, b)
#                 if x < current:
#                     p = b
#                     current = x
#             if n<p:
#                 p=n
#         else:
#             for b in range(l,r+1):
#                 x = f(n, b)
#                 if x < current:
#                     p = b
#                     current = x
#     return p
he = 10**9

for _ in range(int(input())):
    n ,l,r = map(int,input().split())
    for b in range(l,r):
        he = min(he,n-b+1)
    print(he)
