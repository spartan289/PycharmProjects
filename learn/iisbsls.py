def insertionsort(arr):
    c=0
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            c+=1
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(arr)
    print(c)
    return arr
def binaryseach(arr,x):
    low = 0
    n=len(arr)
    high = n-1
    while low<=high:
        mid= low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1


def linearsearch(arr,x):
    n = len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

print("Enter the Elements of list")
li = list(map(int,input().split()))
print("Enter element to found ",end=" ")
x = int(input())
print("Linear Search")

print("Before Sorting")
if(linearsearch(li,x)!=-1):
    print("Element is at Index {}".format(linearsearch(li,x)))
    flag=1
else:
    print("Element not found")
    flag=0
print()
print()
if flag:
    print("After Insertion Sorting")
    print(insertionsort(li))
    print("Binary Sort")
    print("Element is at Index {}".format(binaryseach(li,x)))
else:
    print("After Insertion Sorting")
    print(insertionsort(li))
