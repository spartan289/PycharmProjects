n,Q = map(int,input().split())
a = list(map(int,input().split()))
y = a
for q in range(Q):
    a = y
    x = int(input())
    mul = 1
    for i in range(n):
        mul *= (x-a[i])
    if mul==0:
        print(0)
    elif mul>0:
        print("POSITIVE")
    elif mul<0:
        print("NEGATIVE")




