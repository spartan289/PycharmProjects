from math import pow,pi
def inifinity(r,a,b):
    area = r*r
    c=0
    while r!=0:

        if(c%2==0):
            r=r*a
            area = area + pow(r,2)
            c+=1
        else:
            c+=1
            r=r//b
            area = area + pow(r,2)
    return round(area*pi,6)
for _ in range(int(input())):
    r,a,b = map(int,input().split())
    ans = inifinity(r,a,b)
    print("Case #{}: {}".format(_+1,ans))
