def convertToWave(a, n):
        i = 0
        while i < n - 1:
            a[i], a[i + 1] = a[i + 1], a[i]
            i += 2
        return a
def solve(r, c):
    i=0
    j =c-1
    row = 0
    while i <r and j>=0:
        if a.get(i,j)==1:
            row = i
            j-=1
        else:
            i+=1
    return row

def findpair(root,sum,set):
    if root is None:
        return False
    if findpair(root.left,sum,set):
        return 1
    if sum-root.data in set:
        return 1
    else:
        set.add(root.data)

    return findpair(root.right,sum,set)

    

