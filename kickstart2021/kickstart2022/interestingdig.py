# def sopod(n):
#     product=1
#     sum=0
#     while n!=0:
#         dig = n%10
#         sum += dig
#         product *= dig
#         n=n//10
#     return sum,product
# def interesting(a: int, b: int):
#     c=0
#     for i in range(a,b+1):
#         sum,product = sopod(i)
#         if product%sum==0:
#             c+=1
#     return c
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     print(f"Case #{_+1}: {interesting(a, b)}")
n = int(input())
l = input()
ne=0
t=0
for i in range(n):
    if l[i]=='N':
        ne+=1
    elif l[i]=='T':
        t+=1
if ne>t:
    print("Nutan")
else:
    print('Tusla')

n,m = map(int,input().split())
mass = []
for i in range(m):
    mass.append(int(input()))
mass.sort()
mass.reverse()
dist = [8,1,2,7,6]
# k=n
# p=1
# for i in range(m):
#     if i%2==0:
#         dist.append(k)
#         k-=1
#     if i%2!=0:
#         dist.append(p)
#         p+=1
maxim = 0
for i in range(m):
    for j in range(i+1,m):
        maxim += abs(dist[i]-dist[j])*mass[i]*mass[j]
print(maxim)


print(mass)
print(dist)