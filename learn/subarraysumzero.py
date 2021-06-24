def subarraysumzero(arr: list[int]):
    x=[]
    flag=0

    i=0
    while i<len(arr):
        j=i
        while j<len(arr):
            li = arr[i:j+1]
            if sum(li)==0 and len(li)!=0:
                arr = arr[0:i]+arr[j+1:len(arr)]
                i-=1
            j+=1
        i+=1

    return arr
print(subarraysumzero([2,2,-2,1,-1,-1]))