def maxLen(n, arr):
    maxsum = 0
    hash = {}
    currentsum = 0
    for i in range(n):
        currentsum += arr[i]
        if arr[i] == 0 and maxsum == 0:
            maxsum = 1
        if currentsum == 0:
            maxsum = i+1
        if currentsum in hash:
            maxsum = max(maxsum,i-hash[currentsum])
        else:
            hash[currentsum]=i

    return maxsum
print(maxLen(8,[15,-2,2,-8,1,7,10,23]))