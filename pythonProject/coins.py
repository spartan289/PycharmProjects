n = int(input())
c=0
if n//10>=1:
    d=n//10
    c+=d
    n=n-d*10
if n//5>=1:
    d=n//5
    c+=d
    n=n-d*5
if n//1>=1:
    d=n//1
    c+=d
    n=n-d*1
print(c)
