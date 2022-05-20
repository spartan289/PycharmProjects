

import bisect


def noofpairwithabsdiflessthanmid(a, n, mid):
    result = 0
    for i in range(n):
        if a[i]+mid > a[n-1]:
            result+=n-(i+1)
        else:
            result += bisect.bisect(a, a[i] + mid) - (i+1)
    return result


def kthDiff(a, n, k):
    a.sort()
    low = a[1] - a[0]
    for i in range(1, n - 1):
        low = min(low, a[i + 1] - a[i])
    high = a[n - 1] - a[0]
    while low < high:
        mid = (low + high) >> 1
        if noofpairwithabsdiflessthanmid(a, n, mid) < k:
            low = mid + 1
        else:
            high = mid
    return low
print(kthDiff([5, 7, 9, 3, 4, 2, 1, 8, 9, 10], 10, 10))
