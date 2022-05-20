def solve(i,j):
    return (i+j)%2

for _ in range(int(input())):
    n,i,j= map(int,input().split())
    print(solve(i,j))