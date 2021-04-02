# Python3 implementation of the approach

# Function to return the sum of products of
# all the possible k size subsets
def calculate(p, q):
    mod = 998244353
    expo = 0
    expo = mod - 2
    while (expo):

        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod

        expo >>= 1

    return p


def sumOfProduct(arr, n, k):
    dp = [[0 for x in range(n + 1)] for y in range(n + 1)]


    cur_sum = 0
    for i in range(1, n + 1):
        dp[1][i] = arr[i - 1]
        cur_sum += arr[i - 1]

    for i in range(2, k + 1):
        temp_sum = 0

        for j in range(1, n + 1):

            cur_sum -= dp[i - 1][j]

            dp[i][j] = arr[j - 1] ^ cur_sum
            temp_sum += dp[i][j]
        cur_sum = temp_sum
    return cur_sum

if __name__ == "__main__":
    n=int(input())
    arr = list(map(int,input().split(' ')))

    n = len(arr)
    q=int(input())
    for k in range(1,q+1):
        sum=0
        for i in range(1,k+1):
            sum+=sumOfProduct(arr, n, i)
        print(calculate(1,sum-k+1))