def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxone = 0
    count = 0
    for i in nums:
        if i==0:
            maxone = max(maxone,count)
            count = 0
        else:
            count+=1
    maxone = max(maxone,count)
    return maxone
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))

