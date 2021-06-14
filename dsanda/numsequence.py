def getscoreDifference(numSeq):
    f=0
    s=0
    i=0
    flag=0
    n=len(numSeq)
    while i<n:
        if flag%2==0:
            f+=numSeq[i]
            x=numSeq[i]
                
            numSeq.pop(i)
            if x%2==0:
                numSeq.reverse()
            n-=1
            flag=1
        else:
            s+=numSeq[i]
            x=numSeq[i]
            numSeq.pop(i)
            if x%2==0:
                numSeq.reverse()
            n-=1
            flag=0
    return f-s
import  sys
INT_MAX = sys.maxsize- 1

def findMinimumEffort(developerSkill, k):
    developerSkill.sort()
    n=len(developerSkill)
    effort = 0
    min_sum = INT_MAX
    for i in range(n-k+1):
        for x in range(i,k+i):
            for j in range(k):
                effort += abs(developerSkill[i+j]-developerSkill[x])
            min_sum=min(effort,min_sum)
            effort = 0
    return min_sum
print(findMinimumEffort(developerSkill=[1, 2, 5, 3, 3],k=3))
            
        