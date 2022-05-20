def hillseq(arr,n):
    hash={}
    arr.sort()
    arr.reverse()
    flag=0

    for i in range(n):
        if arr[i] in hash:
            flag=1
            if hash[arr[i]]==2:
                return [-1]
            else:
                hash[arr[i]]+=1
        else:
            hash[arr[i]]=1
    if hash[arr[0]]>1:
        return [-1]
    if flag==1:
        result=[]
        for i in hash:
            result.append(i)
            hash[i]-=1
        j=0
        for i in hash:
            if hash[i]==1:
                result.insert(0,i)
                j+=1
        return result
    if flag==0:
        return arr
for _ in range(int(input())):
    n=int(input())
    arr = list(map(int,input().split()))
    result = hillseq(arr,n)
    for i in result:
        print(i,end=" ")
    print()