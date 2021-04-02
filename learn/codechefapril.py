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
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    c='NO'
    cons='*'*k
    if cons in s:
        c='YES'
    print(c)

