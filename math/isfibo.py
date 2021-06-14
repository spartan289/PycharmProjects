import math


def isPerfectSquare(x):
    sr = int(math.sqrt(x))

    return (sr * sr) == x


def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


for _ in range(int(input())):
    x = int(input())
    if isFibonacci(x):
        print("IsFibo")
    else:
        print("IsNotFibo")
