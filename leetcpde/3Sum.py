def threeSum(nums: list[int]) -> list[list[int]]:
    li = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    l = []
                    l.append(nums[i])
                    l.append(nums[j])
                    l.append(nums[k])
                    li.append(l)
    return li
print(threeSum([-1,0,1,2,-1,-4]))