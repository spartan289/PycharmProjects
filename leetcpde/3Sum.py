def threeSum(nums: list[int]) -> list[list[int]]:
    a = set()
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]]=i

    for i in range(len(nums)):
        for j in range(i+1,len(nums)-1):
            x=-(nums[i]+nums[j])
            if x in hash and hash[x]>j:
                a.add(tuple(sorted([nums[i],nums[j],x])))
    a = list(a)
    return a
print(threeSum([1,2,-2,-1]))