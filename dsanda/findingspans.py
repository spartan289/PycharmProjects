#span finding
def span(arr):
    spanning = []
    for i in range(len(arr)):
        j=1
        while j<=i and arr[i]>arr[i-j]:
            j=j+1
        spanning.append(j)
    return spanning



print(span([6,7,3,4,5,2]))