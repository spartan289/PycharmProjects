t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    x = n - k * (n // k)
    print(x)
