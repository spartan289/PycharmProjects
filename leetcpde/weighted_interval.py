from functools import cmp_to_key
from typing import List


class Solution:
    def findcompatible(self, activity, i):
        for j in range(i - 1, -1, -1):
            if (activity[j][1] <= activity[i][0]):
                return j
        return -1


    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
   
s = Solution()
start = [1,2,3,4,6]
finish=[3,5,10,6,9]
profit=[20,20,100,70,60]
print(s.jobScheduling(start,finish,profit))
