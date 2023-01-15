from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=0
        b=len(numbers)-1
        while(a<b):
            if(numbers[a]+numbers[b]<target):
                a+=1
            elif(numbers[a]+numbers[b]>target):
                b-=1
            else:
                return [a,b]
        return [-1,-1]
sol = Solution()
print(sol.twoSum([2,7,11,15],9))