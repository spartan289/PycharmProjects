T=int(input())

while T>0:
    A,B=map(int,input().split())
    rem = A % B
    T=T-1
    print(rem)