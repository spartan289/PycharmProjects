INT_BITS = 32
def maxXor(a, n):
    index = 0
    for i in range(INT_BITS-1, -1, -1):
        maxInd = index
        maxEle = -2147483648
        for j in range(index,n):
            if (a[j] & (1<<i)!=0) and a[j]>maxEle:
                maxEle = set[j]
                maxInd=j
        if maxEle == -2147483648:
            continue
        temp = a[index]
        a[index]=a[maxInd]
        a[maxInd]=temp

        maxInd = index

        for j in range(n):
            if j!=maxInd and a[j]&(1<<i)!=0:
                a[j]^=a[maxInd]
        index+=1
    res=0
    for i in range(n):
        res = res^a[i]
    return res

