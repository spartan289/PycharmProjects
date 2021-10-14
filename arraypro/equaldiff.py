def max_frequency(arr,n):
    hash = dict()
    for i in range(n):
        if arr[i] in hash.keys():
            hash[arr[i]]+=1
        else:
            hash[arr[i]]=1
    ans = n
    cnt=0
    for element in hash:
        ans = min(ans,n-hash[element])
        cnt+=1

    if cnt>=2:
        ans = min(ans, n-2)
    return ans
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(max_frequency(arr,n))