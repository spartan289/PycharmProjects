def reverse(arr,k):
    c=0
    while(c<len(arr)):
        start = c
        if c>len(arr)-k:
            break
        end = min(k-1+c,len(arr)-1)
        while (start < end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        c+=k
    return arr
print(reverse([1, 2, 3, 4, 5],3))


