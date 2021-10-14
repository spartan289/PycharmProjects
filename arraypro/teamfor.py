from math import floor
for _ in range(int(input())):
    n = int(input())
    s=input()
    t = input()
    if int(s)==0 or int(t)==0:
       print(0)
    else:

        su = str(int(s)+int(t))
        su = list(su.strip())
        su = [int(i) for i in su]
        su.sort()
        c=0
        while n>=0:
            if su[0]==0 and su[n-1]==2:
                c+=1
                su.pop(0)
                su.pop()
                n -= 2
            elif su[0]==1 and su[n-1]==1:
                c+=1
                su.pop(0)
                su.pop()
                n -= 2
            elif su[0]==0 and su[n-1]==1:
                su.pop(0)
                su.pop()
                n -= 2
            elif su[0]==1 and su[n-1]==2:
                c += 1
                su.pop(0)
                su.pop()
                n -= 2
            elif su[0]==2 and su[n-1]==2:
                c += 1
                su.pop(0)
                su.pop()
                n -= 2
            elif su[0]==0 and su[n-1]==0:
                su.pop(0)
                su.pop()
                n -= 2
        print(c)


