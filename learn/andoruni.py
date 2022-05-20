# You are given an array A consisting of N integers.
#
# From array A, we create a new array B containing all pairwise bitwise ANDs of elements from A. That is, B consists of N⋅(N−1)/2 elements, each of the form Ai&Aj for some 1≤i<j≤N.
#
# In array B, we repeat the following process till there is only one element remaining:
#
# Let the current maximum and minimum element of array B be X and Y respectively.
# Remove X and Y from array B and insert X|Y into it.
# Determine the last remaining element in array B.
#
# Here, & denotes the Bitwise AND operation and | denotes the Bitwise OR operation.
def solve(arr, n):
    if n == 1:
        return arr[0]

    ans = 0
    powerof2=1
    for i in range(0, 32):
        k1 = 0
        for j in range(n):
            if arr[j] & (1 << i):
                k1 += 1
        if k1>1:
            ans += powerof2
        powerof2*=2
    return ans


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))
