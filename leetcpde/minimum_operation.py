from typing import List


def minOperations(nums: List[int],x: int)->int:
    prefixSum = [nums[0]]
    n = len(nums)
    for i in range(1,len(nums)):
        sum = nums[i]+prefixSum[i-1]
        prefixSum.append(sum)
    suffixSum = [0 for i in range(n)]
    suffixSum[n-1]=nums[n-1]
    for i in range(n-2,-1,-1):
        suffixSum[i]=suffixSum[i+1]+nums[i]
    print(prefixSum,suffixSum)
minOperations([1,1,4,2,3],5)