def countsubstring(s):
    x = 0
    
    for i in range(len(s)):
        l = 0
        u=0
        for j in range(i,len(s)):

            if s[j].isupper() is True:
                u+=1
            else:
                l+=1
            if u==l:
                x+=1
    return x
                

print(countsubstring("gEEk"))


def gcd(a, b):
    return gcd(b,a%b) if b>0 else a
# def find(l,r):
#
#             if gcd(a,b)==1:
#                 return [a,b]
#     return [-1,-1]

def minop(n):
    op = 0
    while n!=0:
        y = n
        if len(str(y))==1:
            op+=1
            break
        y = [int(x) for x in str(y)]
        m1 = max(y)
        n = n-m1
        op+=1
    return op

def pairs(n, arr):
        # code here 
        c = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] ^ arr[j] < (arr[i] and arr[j]):
                    c += 1
        return c
print(pairs(4,[6,2,5,3]))