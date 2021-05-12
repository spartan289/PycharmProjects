def binarysearch(li,n,x):
    i=n//2
    if x>li[n-1] or x<li[0]:
        return False
    if x==li[i]:
        return True

    if x<li[i]:
        if(binarysearch(li[:i],n-i,x)):
            return True
        else:
            return False
    elif x>li[i]:
        if(binarysearch(li[i:],n-i,x)):
            return True
        else:
            return False

print(binarysearch([1,2,4,6,8,10],6,2))