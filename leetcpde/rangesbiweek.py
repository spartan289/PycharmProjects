def isCovered(ranges, left, right):
    c=0
    for i in range(left,right+1):
        for l,r in ranges:
            if l<=i <= r:
                c+=1
                break
    return c == right-left+1
ranges= [[1,2],[3,4],[5,6]]
def chalkreplacer(chalk,k):
    x = sum(chalk)
    p=k%x
    c=0
    if k%x==0:
        return 0
    for i in range(len(chalk)):
        c=c+chalk[i]
        if c>p:
            return i
print(chalkreplacer([3,4,1,2],25))