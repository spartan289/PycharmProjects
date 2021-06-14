def summation(a, i, x, n):
    s = 0
    if x == 'l':
        for j in range(i):
            s += a[j]
    elif x == 'r':
        for j in range(i + 1, n):
            s += a[j]
    return s



for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    flag = "NO"
    for i in range(n):
        x = summation(li, i, 'l', n)
        y = summation(li, i, 'r', n)
        if x == y:
            flag = "YES"
            break
    print(flag)
