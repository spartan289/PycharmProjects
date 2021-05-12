def towerofhanoi(numberofDisks, startpeg=1, endpeg=3):
    if numberofDisks:
        towerofhanoi(numberofDisks - 1, startpeg, 6 - startpeg - endpeg)
        print("Move disk %d from peg %d to peg %d" % (numberofDisks, startpeg, endpeg))
        towerofhanoi(numberofDisks - 1, 6 - startpeg - endpeg, endpeg)


towerofhanoi(numberofDisks=3)
