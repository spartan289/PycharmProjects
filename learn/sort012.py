class Solution:
    def sort012(self,arr,n):
        # code here
        low = 0
        mid = 0
        while mid<=n-1:
            if arr[mid]== 0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid = mid+1
            else:
                arr[mid],arr[n-1] = arr[n-1],arr[mid]
                n-=1
        return arr



so = Solution()
print(so.sort012([0,2,1,2,0],5))

