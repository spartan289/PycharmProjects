def maximiseSum(arr,n,k):
    for i in range(n):
        if arr[i]<0 and k>0:
            arr[i]=arr[i]*-1
            k-=1
    if k>0:
        if k%2==0:
            return sum(arr)
        else:
            return sum(arr)-2*min(arr)
    else:
        return sum(arr)
print(maximiseSum([5, -2, 5, -4, 5, -12, 5, 5, 5, 20],10,5))


