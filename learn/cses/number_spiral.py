for _ in range(int(input())):
    row, col = map(int, input().split())
    n = max(row, col)
    nmax = n * n
    nmin = (n - 1) * (n - 1) + 1
    nbw = (nmax + nmin) // 2
    if n % 2 != 0:
        if col<n:
            print(nbw-(n-col))
        else:
            print(nbw+(n-row))
    else:
        if col<n:
            print(nbw+(n-col))
        else:
            print(nbw-(n-row))

