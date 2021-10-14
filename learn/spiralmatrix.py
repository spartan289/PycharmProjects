def findk(a,m, n,c):
    k = 0
    l = 0
    count = 0

    while (k < m and l < n):
        for i in range(l, n):
            count += 1

            if (count == c):
                return a[k][i]

        k += 1

        for i in range(k, m):
            count += 1
            if (count == c):
                return a[i][n - 1]
        n -= 1

        if (k < m):
            for i in range(n - 1, l - 1, -1):
                count += 1
                if (count == c):
                    return a[m - 1][i]
            m -= 1

        if (l < n):
            for i in range(m - 1, k - 1, -1):
                count += 1
                if (count == c):
                    return a[i][l]
            l += 1
print(findk([[1, 2, 3], [4, 5, 6], [7, 8, 9]],3,3,4))