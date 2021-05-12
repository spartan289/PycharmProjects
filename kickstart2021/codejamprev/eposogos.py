import math


def func(x,y,d):
    if d==0:
        return 0
    if x==0 and y==0:
        return 0
    e=abs(x+d)+abs(y)
    w=abs(x-d)+abs(y)
    n=abs(x)+abs(y+d)
    s=abs(x)+abs(y-d)
    dict = {e:'W',w:'E',n:'S',s:'N'}

    mov = min(e,w,n,s)
    dir=(dict.get(mov))

    if dir=='N':
        x=x
        y=y-d
    elif dir=='S':
        x=x
        y=y+d
    elif dir=='W':
        x=x+d
        y=y
    elif dir=='E':
        x=x-d
        y=y

    func(x,y,d/2)
    print(dir,end="")
for _ in range(int(input())):
    x,y=map(int,input().split())
    z=(x+y)
    if z%2!=0:
        i=0
        n=0

        while(True):
            if (abs(x)+abs(y))<math.pow(2,i):
                n=math.pow(2,i-1)
                break
            i+=1
        print("Case #{}: ".format(_+1),end="")
        func(x,y,n)
        print()
    else:
        print("Case #{}: ".format(_ + 1),end="")
        print("IMPOSSIBLE")




