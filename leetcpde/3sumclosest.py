def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    diff = 10000
    li = []
    d = 0
    for a in range(len(nums)-2):
        b = a+1
        c = len(nums)-1
        while b<c:
            i=nums[a]+nums[b]+nums[c]
            if abs(target-i)<diff:
                d = i
                diff = abs(target-i)
            if i < target:
                b+=1
            else:
                c-=1
    return d
print(threeSumClosest([-1,2,1,-4],1))