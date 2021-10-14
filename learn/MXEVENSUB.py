for _ in range(int(input())):
    n = int(input())
    sum = (n*(n+1))//2
    if sum%2==0:
        print(n)
    else:
        print(n-1)