def maxProductDifference(nums: list[int]) -> int:
    nums.sort()
    w,x,y,z=nums[0],nums[1],nums[len(nums)-2],nums[len(nums)-1]
    return y*z - w*x
# print(maxProductDifference([4,2,5,9,7,4,8]))

def rotateGrid(grid: list[list[int]], k: int) -> list[list[int]]:
    r = len(grid)
    c = len(grid[0])
    lc = min(r,c)//2
    layer = []
    for i in range(lc):
        circle = []
        circle += grid[i][i:c-i]
        circle += [grid[k][-1-i] for k in range(i+1,r-1-i)]
        circle += grid[-1-i][i:c-i][::-1]
        circle += [grid[k][i] for k in range(r-2-i,i,-1)]
        ro = k %len(circle)
        circle = circle[ro:]+circle[:ro]
        cnt = 0
        for idx in range(i,c-i):
            grid[i][idx] = circle[cnt]
            cnt+=1
        for idx in range(i+1,r-1-i):
            grid[idx][-1-i] = circle[cnt]
            cnt+=1
        for idx in range(c-i-1,i-1,-1):
            grid[-1-i][idx] = circle[cnt]
            cnt+=1
        for idx in range(r-2-i,i,-1):
            grid[idx][i] = circle[cnt]
            cnt+=1
    return grid

print(rotateGrid([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],2))
