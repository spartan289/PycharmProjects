def Kclosest(arr, n, x, k):
    # Your code goes here
    arr.sort()
    ans = []
    for i in range(n):
        ans.append((abs(arr[i]-x),i))
    ans.sort()
    result = []
    for j in range(k):
        result.append(arr[ans[j][1]])
    result.sort()
    return result
print(Kclosest([-21, 21, 4, -12, 20],5,0,4))