def binaryseach(arr,l,r,x):
    while l<=r:
        mid = (l+r)//2
        if arr[mid]<x:
            l=mid+1
        elif arr[mid]>x:
            r = mid-1
        else:
            return mid
    return -1
def pivotpt(nums:list[int])-> int:
    for i in range(len(nums)-1):
        if nums[i+1]<nums[i]:
            return i
    return -1

def search(nums:list[int],target: int)->int:
    high1 = pivotpt(nums)
    if high1 == -1:
        return binaryseach(nums,0,len(nums)-1,target)

    if target>nums[0]:
        return binaryseach(nums,0,high1,target)
    if target<nums[0]:
        return binaryseach(nums,high1+1,len(nums)-1,target)
    if target==nums[0]:
        return 0
print(search([3,1],3))



