#q1
# a,b,c=map(int,input().split())
# if a==b or b==c or c==a or a==b==c:
#     print("YES")
# else:
#     print("NO")
#q2
# for _ in range(int(input())):
#     k1,k2,k3,v=map(float,input().split())
#     speed = k1*k2*k3*v
#     time = 100/speed
#     time = round(time,2)
#     if time >= 9.58:
#         print("NO")
#     else:
#         print("YES")

#q3
# for _ in range(int(input())):
#     n,k=map(int,input().split())
#     s=input()
#     c='NO'
#     for i in range(n-k+1):
#         con=s[i:i+k]
#         if con =='*'*k:
#             c='YES'
#             break
#     print(c)
#type2
# for _ in range(int(input())):
#     n,k=map(int,input().split())
#     s=input()
#     c='NO'
#     cons='*'*k
#     if cons in s:
#         c='YES'
#     print(c)
# type 3
#
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     s= input()
#     flag=0
#     count = 0
#     for i in range(n):
#         if s[i] == '*':
#             count+=1
#         else:
#             if count>=k:
#                 flag=1
#                 break
#             else:
#                 count=0
#     if count>=k:
#         flag=1
#     if flag==1:
#         print("YES")
#     else:
#         print("NO")

# dice and problem
def dice(n):
    if n==1:
        return 20
    elif n==2:
        return 36
    elif n==3:
        return 51
    elif n==4:
        return 60
    else:
        r=n%4
        s=60*(n//4)-4*(n-4)
        if r==1:
            s=s+dice(1)
        elif r==2:
            s=s+dice(2)
        elif  r==3:
            s=s+dice(3)
        return s
for _ in range(int(input())):
    print(dice(int(input())))
