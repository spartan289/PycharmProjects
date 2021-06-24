def maxArea(height: list[int])->int:
    maxi = 0
    current =0
    for i in range(len(height)):
        for j in range(i,len(height)):
            current = abs(i-j)*min(height[i],height[j])
            maxi = max(current,maxi)
    return maxi
print(maxArea([1,2,1]))
