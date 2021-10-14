def subset(arr,l,r,k):
    if l<r:
        prod=1
        for i in range(l,r+1):
            prod *= arr[i]
