def towerofhanoi(numberofDisks, startpeg=1, endpeg=3):
    if numberofDisks:
        towerofhanoi(numberofDisks - 1, startpeg, 6 - startpeg - endpeg)
        print(startpeg, endpeg)
        towerofhanoi(numberofDisks - 1, 6 - startpeg - endpeg, endpeg)

n = int(input())
print(2**(n)-1)
towerofhanoi(numberofDisks=n)
