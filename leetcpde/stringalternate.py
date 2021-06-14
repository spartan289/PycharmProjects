def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1


def flip(ch):
    return '1' if (ch == '0') else '0'

def getFlipWithStartingCharcter(str, expected):
    flipCount = 0
    for i in range(len(str)):

        if (str[i] != expected):
            flipCount += 1

        expected = flip(expected)
    return flipCount

def minFlipToMakeStringAlternate(str):

    return min(getFlipWithStartingCharcter(str, '0'),
               getFlipWithStartingCharcter(str, '1'))

def minFlips(s: str) -> int:
    z = minFlipToMakeStringAlternate(s)
    c=0
    n=len(s)
    while c<n:

        x =list(s)
        a = x[0]
        x.pop(0)
        x.append(a)
        s = listToString(x)
        z = min(minFlipToMakeStringAlternate(s),z)
        c+=1
    return z
print(minFlips("01001001101"))