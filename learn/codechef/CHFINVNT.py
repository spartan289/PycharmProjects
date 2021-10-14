for _ in range(int(input())):
    n, p, k = map(int, input().split())
    day = 0
    x = p%k
    if n%k<p%k:
        day = (n%k) * (n//k+1) + (p%k-n%k)*(n//k)+(p//k+1)
    else:
        day = p%k*(n//k+1)+(p//k)+1

    print(day)

