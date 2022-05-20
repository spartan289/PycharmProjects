from typing import List

def length_ofclearpath(grid,i,j):
    if(grid[i][j]==0):
        return 1+grid(i+1,j+1)
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    q=[]
    q.append([[0,0],1])
    n=len(grid)
    mincount=1000
    m=len(grid[0])

    visited = [[False for i in range(n)] for j in range(n)]
    visited[0][0]=True
    if grid[0][0]==1 or grid[n-1][n-1]:
        return -1
    while len(q)!=0:
        ind, c = q.pop(0)
        if(ind[0] == n-1 and ind[1]==n-1 ):
            print(c)
            mincount = min(mincount,c)
        if(ind[0]+1<m and ind[0]+1>-1 and ind[1]+1<n and ind[1]+1>-1 and visited[ind[0] + 1][ind[1] + 1] == False):
            if grid[ind[0]+1][ind[1]+1]==0 :
                q.append([[ind[0]+1,ind[1]+1],c+1])
                visited[ind[0] + 1][ind[1] + 1] = True
        if(ind[0]-1<m and ind[0]-1>-1 and ind[1]-1<n and ind[1]-1>-1 and visited[ind[0] - 1][ind[1] - 1] ==False):
            if grid[ind[0]-1][ind[1]-1]==0 :
                q.append([[ind[0]-1,ind[1]-1],c+1])
                visited[ind[0] - 1][ind[1] - 1] =True
        if(ind[0]-1<m and ind[0]-1>-1 and ind[1]+1<n and ind[1]+1>-1 and visited[ind[0]-1][ind[1]+1]==False):
            if grid[ind[0]-1][ind[1]+1]==0:
                q.append([[ind[0]-1,ind[1]+1],c+1])
                visited[ind[0]-1][ind[1]+1]=True

        if(ind[0]+1<m and ind[0]+1>-1 and ind[1]-1<n and ind[1]-1>-1 and visited[ind[0] + 1][ind[1] - 1] ==False):
            if grid[ind[0]+1][ind[1]-1]==0 :
                q.append([[ind[0]+1,ind[1]-1],c+1])
                visited[ind[0] + 1][ind[1] - 1] =True
        if(ind[0]-1<m and ind[0]-1>-1 and ind[1]<n and ind[1]>-1 and visited[ind[0] - 1][ind[1]] ==False):
            if grid[ind[0]-1][ind[1]]==0:
                q.append([[ind[0]-1,ind[1]],c+1])
                visited[ind[0] - 1][ind[1]] =True
        if(ind[0]+1<m and ind[0]+1>-1 and ind[1]<n and ind[1]>-1 and visited[ind[0] + 1][ind[1]] ==False):
            if grid[ind[0]+1][ind[1]]==0:
                q.append([[ind[0]+1,ind[1]],c+1])
                visited[ind[0] + 1][ind[1]] =True
        if(ind[0]<m and ind[0]>-1 and ind[1]-1<n and ind[1]-1>-1 and visited[ind[0]][ind[1] - 1] ==False):
            if grid[ind[0]][ind[1]-1]==0 :
                q.append([[ind[0],ind[1]-1],c+1])
                visited[ind[0]][ind[1] - 1] =True
        if(ind[0]<m and ind[0]>-1 and ind[1]+1<n and ind[1]+1>-1 and visited[ind[0]][ind[1] + 1] ==False):
            if grid[ind[0]][ind[1]+1]==0:
                q.append([[ind[0],ind[1]+1],c+1])
                visited[ind[0]][ind[1] + 1] =True
    if mincount==1000:
        return -1
    else:
        return mincount
grid = [[1,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))