def repeatedStringMatch(A, B):
    c=1
    sr = A
    while len(sr)<len(B):
        sr = sr+A
        c+=1
    if B in sr:
        return c
    sr = sr+A
    c+=1
    if B in sr:
        return c
    return -1

print(repeatedStringMatch("aa","a"))

        
