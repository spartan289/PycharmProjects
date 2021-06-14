for _ in range(int(input())):
    X=list(map(int, input().split()))
    g=X[0]
    p=X[1]
    X.pop(0)
    X.pop(1)
    day=0
    n=10

    while n>0:
        if p>X[n-1]:
            d+=1



