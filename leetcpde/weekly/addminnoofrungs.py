import math
def addRungs(rungs: list[int], dist: int) -> int:
    rung = 0
    i=1
    if rungs[0]-dist>=1:
        rung += math.ceil((rungs[0]) / dist) - 1

    while i<len(rungs):

        if rungs[i]-rungs[i-1]>dist:
            rung += math.ceil((rungs[i]-rungs[i-1])/dist)-1
        i+=1
    return rung
print(addRungs([15,26,29],4))
