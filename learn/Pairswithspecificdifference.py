def maxSumPairWithDifferenceLessThanK(arr, N, K):
    ans = 0
    arr.sort()
    i=N-1
    while(i>0):
        if arr[i]-arr[i-1]<K:
            ans +=arr[i]
            ans+=arr[i-1]
            i-=1
        i-=1
    return ans


print(maxSumPairWithDifferenceLessThanK([3,5,10,15,17,12,9],7,4))
