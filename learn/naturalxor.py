def xor(n):
    if n==1:
        return [1, 1]
    elif n==2:
        return [ 2, 2, 1]
    elif n==3:
        return [0]
for _ in range(int(input())):
    n=int(input())
    nx = [i+1 for i in range(n)]
    while True:
        n=n^(n-1)
        for i in nx:
            if i>n:
                nx.remove(i)

        print(nx)
        if n==0:
            break
