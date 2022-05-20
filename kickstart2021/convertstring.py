def findclosest(arr,n, target):
    if target<=arr[0]:
        return arr[0]
    if target>=arr[n-1]:
        return arr[n-1]
    i=0
    j=n
    mid=0
    while i<j:
        mid = (i+j)//2
        if arr[mid]==target:
            return arr[mid]
        if target<arr[mid]:
            if mid>0 and target>arr[mid-1]:
                return getClosest(arr[mid-1],arr[mid],target)
            j=mid
        else:
            if mid<n-1 and target<arr[mid+1]:
                return getClosest(arr[mid],arr[mid+1],target)
            i=mid+1
    return arr[mid]
def getClosest(val1,val2,target):
    if (ord(target) - ord(val1) >= ord(val2) - ord(target)):
        return val2
    else:
        return val1
def convert(s,f):
    count=0
    for i in s:
        mini = 100000
        for j in f:
            cur = abs(ord(j)-ord(i))
            if cur>=13:
                cur=abs(cur-26)
            if cur<mini:
                mini=cur
        count+=mini
    return count
for _ in range(int(input())):
    s = input()
    f = input()
    result = convert(s, f)
    print(f'Case #{_+1}: {result}')