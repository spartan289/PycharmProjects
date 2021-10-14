def maxCandy(height, n):
    M= 0
    i,j = 0,n-1
    while i<j:
        x= min(height[i],height[j])*(abs(i-j)-1)
        M = max(x,M)
        if height[i]>height[j]:
            j-=1
        else:
            i+=1
    return M
print(maxCandy([2, 1, 3, 4, 6, 5],6))

