def power(x, y, p):
    res = 1

    x = x % p

    if x == 0:
        return 0

    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p

        y = y >> 1
        x = (x * x) % p

    return res


for _ in range(int(input())):
    n = int(input())
    ans = power(2, n - 1, 1000000007)
    print(ans)
