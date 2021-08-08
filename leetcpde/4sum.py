def fourSum(nums: list[int], target: int):
    li = []
    nums.sort()
    for f in range(len(nums)-3):
        for s in range(f+1,len(nums)-2):
            i = s+1
            j = len(nums)-1
            while i<j:
                if nums[i]+nums[j] == target-nums[f]-nums[s]:
                    x = [nums[f],nums[s],nums[i],nums[j]]
                    if x not in li:
                        li.append([nums[f],nums[s],nums[i],nums[j]])
                if nums[i]+nums[j]<target-nums[f]-nums[s]:
                    i+=1
                else:
                    j-=1
    return li
print(fourSum([2,2,2,2,2,2],8))
                    