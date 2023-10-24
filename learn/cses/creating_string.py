def generate_string(s,l,r,a):
    if l==r:
        a.append(s)
    else:
        for i in range(l,r+1):
            s[l],s[i]=s[i],s[l]
            generate_string(s,l+1,r,a)
            s[l],s[i]=s[i],s[l]




def factorial(n):
    if n==1:
        return 1
    return  n*factorial(n-1)
s = input()
n = len(s)
freq = {}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
base=1
for i in freq:
    base *= factorial(freq[i])
count = factorial(n)//base
print(count)
a=[]
generate_string(s,0,n-1,a)