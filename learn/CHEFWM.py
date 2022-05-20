from math import sqrt


def chefm(n, m):
    c = 0
    i = 2
    a = set()
    while m % 2 == 0:
        a.add(2)
        m = m // 2
    for i in range(3, int(sqrt(m)) + 1, 2):
        while m % i == 0:
            m = m // i
            a.add(i)
    if m>2:
        a.add(m)
    c = len(a)
    if c==0:
        return 0
    if n<c:
        return n
    else:
        while n%c != 0:
            c -= 1
    return c


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(chefm(n, m))
