MAX_CHAR = 256


def maximumChars(str1):
    n = len(str1)
    res = 0

    firstInd = [-1 for i in range(MAX_CHAR)]

    for i in range(n):
        first_ind = firstInd[ord(str1[i])]

        if (first_ind == -1):
            firstInd[ord(str1[i])] = i


        else:
            res = max(res, abs(i - first_ind - 1))

    return res


t = int(input())
for _ in range(t):
    str1 = input()
    print(maximumChars(str1))