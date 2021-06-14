def twosum(nums,target):
    h={}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num]=i
        else:
            return[h[n],i]
print(twosum([2,11,15,7],9))
