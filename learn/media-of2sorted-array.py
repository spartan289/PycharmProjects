import math
class Solution:
    def MedianOfArrays(self, array1, array2):
        # code here
        if len(array2) < len(array1):
            self.MedianOfArrays(array2, array1)
        low = 0
        high = len(array1)
        while low <= high:
            partitionx = (low + high) // 2
            partitiony = int((len(array1) + len(array2)) / 2 - partitionx)

            maxLeftx = -math.inf if partitionx == 0 else array1[partitionx - 1]
            minRightX = math.inf if partitionx == len(array1) else array1[partitionx]

            maxlefty = -math.inf if partitiony == 0 else array2[partitiony - 1]
            minRightY = +math.inf if partitiony == len(array2) else array2[partitiony]

            if maxLeftx <= minRightY and maxlefty <= minRightX:
                if (len(array1) + len(array2)) % 2 == 0:
                    return (max(maxLeftx, maxlefty) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftx, maxlefty)
            elif maxLeftx > minRightY:
                high = partitionx - 1
            else:
                low = partitionx + 1
sol = Solution()
print(sol.MedianOfArrays([1,2,3,5],[4,6]))
