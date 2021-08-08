def lengthOfLIS(nums: list[int]) -> int:
    i=0
    j=1
    sum=1
    currentsum=0
    while j<len(nums):
        if nums[j]>nums[i]:
            sum+=1
            i+=1
            j+=1
        else:
            currentsum = max(sum,currentsum)
            sum=0
            i=j
            j+=1
    return currentsum
print(lengthOfLIS([10,9,2,5,3,7,101,18]))


