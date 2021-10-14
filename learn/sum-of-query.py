def querySum(n,arr,q,queries):
    ar = []
    for i in range(0,q*2,2):
        l = queries[i]
        r = queries[i+1]
        x = sum(arr[l-1:r])
        ar.append(x)
    return ar
print(querySum(4,[1,2,3,4],2,[1,4,2,3]))

