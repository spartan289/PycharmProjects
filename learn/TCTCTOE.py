def check(A):
    c=0
    for i in range(3):
        if A[i][0]==A[i][1] and A[i][1]==A[i][2]:
            c+=1
        if A[0][i]==A[1][i] and A[1][i]==A[2][i]:
            c+=1
    if A[0][0]==A[1][1] and A[1][1]==A[2][2]:
        c+=1
    if A[2][0] == A[1][1] and A[1][1] == A[0][2]:
        c+=1
    return c

def dashkikahani(A):
    c=0
    for i in range(3):
        for j in range(3):
            if A[i][j]=='_':
                if c==0:
                    A[i][j]='X'
                    c=1

                elif c==1:
                    A[i][j]='O'
                    c=0
    if check(A) == 1:
        return 1
    if check(A) >= 2:
        return 3
    if check(A) == 0:
        return 2


t=int(input())
for _ in range(t):
    matrix = []
    s1=input()
    s2=input()
    s3=input()
    a=[]
    b=[]
    c=[]
    for i in range(len(s1)):
        a.append(s1[i])
        b.append(s2[i])
        c.append(s3[i])
    matrix.append(a)
    matrix.append(b)
    matrix.append(c)
    print(dashkikahani(matrix))
