def noofpath(a,b):
    matrix = [[0 for i in range(b)] for i in range(a)]
    for i in range(a):
        matrix[i][0]=1
    for j in range(b):
        matrix[0][j]=1
    for i in range(1,a):
        for j in range(1,b):
            matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
    return matrix[a-1][b-1]
