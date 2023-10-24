from typing import List


def runningSum(nums: List[int]) -> List[int]:
    rsum = [nums[0]]
    for i in range(1, len(nums)):
        rsum.append(nums[i] + rsum[i - 1])
    return rsum
print(runningSum([1,2,3,4]))