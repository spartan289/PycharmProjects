def recursion(x, y):
    if y == 3:
        print(x)
    else:
        for i in range(y, 4):
            x[i], x[y] = x[y], x[i]
            recursion(x, y + 1)
            x[i], x[y] = x[i], x[y]


def withrepition(A, s, l, index):
    n = len(A)
    for i in range(n):
        s[index] = A[i]
        if index == l:
            print(s)
        else:
            withrepition(A, s, l, index + 1)


withrepition([1, 2, 3], [0 for i in range(3)], 2, 0)

li = [1, 2, 3, 4]
