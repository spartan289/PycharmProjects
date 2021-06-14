from math import sqrt
for _ in range(int(input())):
    n=int(input())
    flag=1
    d = sqrt(1+8*n)
    if d.is_integer():
        x=(-1+d)//2
        print("Go on Bob",format(int(x)))
    else:
        print("Better Luck Next Time")