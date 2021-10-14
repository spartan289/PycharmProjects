def vdate(d,l,r):
    if d<l:
        print("Too Early")
    elif d>r:
        print("Too Late")
    else:
        print("Take second dose now")

def twodish(n,a,b,c):
    x = n-c
    if n<=b:
        if a>=x:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
import math

def alboface(n):
    c=0
    while n!=0:
        if n%2==0:
            while n%2==0:
                n=n/2
        else:
            n-=1
        c+=1
    if c%2==0:
        print("Bob")
    else:
        print("Alice")

for _ in range(int(input())):
    n = int(input())
    alboface(n)
