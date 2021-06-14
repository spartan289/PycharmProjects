def singleNumber(nums: list[int]) -> int:
    hsh = {}
    for i in nums:
        if i in hsh:
            hsh[i] = 2
        else:
            hsh[i] = 1
    for i in nums:
        if hsh[i] == 1:
            return i
print(singleNumber([2,2,1,3,3]))