def reverseArray(a):
    for i in range(0,int(len(a)/2)):
        other=len(a)-i-1
        temp=a[i]
        a[i]=a[other]
        a[other]=temp
    for i in a:
        print(i,end=" ")