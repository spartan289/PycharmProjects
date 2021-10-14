def countTriplets(arr,n,sum):
    arr.sort()
    triplets = 0
    for i in range(n-2):
        j=i+1
        k=n-1
        while j<k:
            if arr[i]+arr[j]+arr[k]<sum:
                triplets+=k-j
                j+=1
            else:
                k-=1

    return triplets
print(countTriplets([-2, 0, 1, 3],4,2))

