def print2largest(arr,
                  arr_size):
    if (arr_size < 2):
        return

    arr.sort()

    for i in range(arr_size - 2,-1, -1):
        if (arr[i] != arr[arr_size - 1]):
            return arr[i]
def minCost(A):
    c=0
    while(True):
        a =max(A)
        b = print2largest(A,len(A))
        A[A.index(a)]=a-b
        if (a-b)==0:
            return c
        c+=1
print(minCost([5,1,3]))
