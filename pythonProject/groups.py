import math
def countBits(number):
    return int((math.log(number) / math.log(2)) + 1)
t=int(input())
for _ in range(t):
    c=int(input())
    b=countBits(c)
    l=[]
    r=[]
    for i in range(2**(b-1)-1,2**b):
        l.append(i)
    for i in range(2**(b-1)-1,2**b):
        if c^l[i-2**(b-1)-1] in l:
            x=c^l[i-2**(b-1)-1]

            r.append(x*l[i-2**(b-1)-1])
    print(max(r))
