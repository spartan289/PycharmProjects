import bisect

def minInsandDels(a,b,n,m):
    def binarysearch(arr,x):
        l = 0
        r = len(arr)-1
        while l<=r:
            mid= l + (r-l)//2
            if arr[mid]==x:
                return mid
            elif arr[mid]<x:
                l = mid+1
            else:
                r=mid-1
        return -1
    def lcs(a,b,n,m):
                
        dp  = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(1,n+1):
            j = binarysearch(b,a[i-1])
            if j!=-1:
                dp[i][j+1] = max(dp[i][j], dp[i - 1][j+1])
                dp[i][j+1] = dp[i - 1][j] + 1


        return dp[m][n]

    x = lcs(a,b,n,m)
    x = n+m-2*x
    return x
print(minInsandDels([1, 2, 5, 3, 1],[1,3,5],5,3))




