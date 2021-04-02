def lrslength(X, m, n):
    if m==0 or n==0:
        return 0
    if X[m-1] == X[n-1] and m!=n:
        return lrslength(X,m-1,n-1)+1
    return max(lrslength(X,m,n-1),lrslength(X,m-1,n))
s=input()
m=len(s)
print(lrslength(s,m,m))