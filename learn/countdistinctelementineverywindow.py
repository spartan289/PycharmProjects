def countDistinct(a,n,k):
    i=0
    j=k-1
    hash = {}
    result = []
    c = 0
    for p in range(k):
        if a[p] in hash:
            hash[a[p]]+=1
        else:
            hash[a[p]]=1
            c+=1
    result.append(c)
    j+=1
    i+=1
    while i<n and j<n:
        x=a[i-1]
        if hash[a[i-1]]>1:
            hash[a[i-1]]-=1
        else:
            del hash[a[i-1]]

        if a[j] in hash:
            hash[a[j]]+=1
        else:
            hash[a[j]]=1

        i+=1
        j+=1
        result.append(len(hash))

    return result
print(countDistinct([1,2,1,3,4,2,3],7,4))

