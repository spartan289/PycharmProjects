def minNumber(arr, low, high):
    a = low
    b=high+1
    while(a<b):
        c=(b-a)//2+a
        if(arr[c]<=arr[b]):
            b=c
        else:
            a=c+1
    if a==high+1:
        return arr[0]
    else:
        return arr[a]