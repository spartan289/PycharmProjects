def twosum(nums,target):
    h={}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num]=i
        else:
            return[h[n],i]
def twoSum(nums, target: int) :
        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                return [i,hash[nums[i]]]
            else:
                hash[target-nums[i]]=i
print(twoSum([2,11,15,7],9))
