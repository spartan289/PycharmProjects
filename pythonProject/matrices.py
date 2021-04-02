def diagonalDifference(arr):
    # Write your code here
    s1=0
    s2=0
    n=len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                s1+=arr[i][j]
            if (i+j)==(n-1):
                s2+=arr[i][j]
    x=(abs(s2-s1))
    return x
n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)