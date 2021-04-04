# for _ in range(int(input())):
#     n=int(input())
#     li=list(map(int, input().split()))
#     b=0
#     j=0
#     for i in range(n):
#         if i%2==0:
#            if li[i]%2==0:
#                b+=1
#         else:
#             if li[i]%2==0:
#                 j+=1
#     if b>j:
#         print("Ben")
#     elif b<j:
#         print("Jim")
#     else:
#         print("Ben")
# q2

# n=int(input())
# sum=0
# while n>=10:
#     sum += n % 10
#     n=n//10
# print(sum+n)
# q4
# for _ in range(int(input())):
#     n=int(input())
#     if n%4==0:
#         if n%100==0:
#             if n%400==0:
#                 print("Yes")
#             else:
#                 print("No")
#         else:
#             print("Yes")
#     else:
#         print("No")
# q5
# p=0
# t=0
# for _ in range(int(input())):
#     pra,tina=map(int,input().split())
#     if pra>tina:
#         p+=1
#     elif tina>pra:
#         t+=1
# if p>t:
#     print("Pragya")
# elif t>p:
#     print("Tina")
# else:
#     print("Draw")
# q6
import math
def fascinating(n):
    ar = [0]*10
    while n>0:
        digit=math.floor(n%10)
        if ar[digit]:
            return False
        ar[digit] = 1
        n=n/10
    return True
for _ in range(int(input())):
    n=int(input())
    while fascinating(n) is True:
        n+=1
    n+=1
    print(n)

