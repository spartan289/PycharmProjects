def minJump(arr,n):
    if n<=1:
        return 0
    if arr[0]==0:
        return -1
    maxrange = arr[0]
    steps = arr[0]
    jump=1
    for i in range(1,n):
        if i==n-1:
            return jump
        maxrange=max(maxrange,i+arr[i])
        steps-=1
        if steps==0:
            jump+=1
            if i>=maxrange:
                return -1
            steps = maxrange-1
    return -1
