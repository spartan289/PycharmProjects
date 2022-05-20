def countTripletslessthanx(arr,n,val):
    arr.sort()
    ans = 0
    for i in range(n-2):
        j = i+1
        k = n-1
        while j!=k:
            sum = arr[i]+arr[j]+arr[k]
            if sum>val:
                k-=1
            else:
                ans+=k-j
                j+=1
    return ans
def countTriplets(arr, N, L, R):
    if N<2:
        return 0
    return countTripletslessthanx(arr,N,R)-countTripletslessthanx(arr,N,L-1)
