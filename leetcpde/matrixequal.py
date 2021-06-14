
def findRotation(mat, target) -> bool:
    R = len(mat)
    C = len(mat[0])
    
    def reverseColumns(mat):
        for i in range(C):
            j = 0
            k = C - 1
            while j < k:
                t = mat[j][i]
                mat[j][i] = mat[k][i]
                mat[k][i] = t
                j += 1
                k -= 1
    
    def transpose(mat):
        for i in range(R):
            for j in range(i, C):
                t = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = t
    
    def rotate90(mat):
        transpose(mat)
        reverseColumns(mat)
    
    
    for i in range(4):
        if mat == target:
            return True
        else:
            rotate90(mat)
    return False
print(findRotation([[0,1],[1,1]], [[1,0],[0,1]]))