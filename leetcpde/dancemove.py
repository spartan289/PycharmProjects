def move(x,y):
    if y>=x:
        diff = y-x
        if diff%2==0:
            return (y-x)//2
        else:
            return (y-x+1)//2+1
    else :
        diff = x-y
        return diff
for _ in range(int(input())):
    x,y = map(int,input().split())
    print(move(x,y))