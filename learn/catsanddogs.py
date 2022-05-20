def dofandcat(n,d,c,m,s):
    D=0
    for i in range(n):
        if s[i]=='D':
            D+=1
    if D==0:
        return "YES"
    else:
        i = 0
        while i<n:
            if s[i]=='C':
                if c==0:
                    break

                else:
                    c-=1
            elif s[i]=='D':
                if d==0:
                    break
                else:
                    D-=1
                    d-=1
                    c+=m

            i+=1
        if D==0:
            return "YES"
        else:
            return "NO"
for _ in range(int(input())):
    n,d,c,m = map(int,input().split())
    s = input()
    print(f'Case #{_+1}: {dofandcat(n,d,c,m,s)}')

def kadanes(b,x):
    windowsum=0
    i=j=0
    li=[]
    k=0
    while i<len(b):
        while j<len(b) and windowsum<k:
            j+=1
            windowsum += b[j]
            if windowsum==k:
                li.append(b[i:j+1])


def bananabunches(n,b,k):
