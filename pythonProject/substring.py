def countSubString(s, c, k):
    # left and right counters for characters
    # on both sides of subwindow
    leftCount = 0
    rightCount = 0

    # left and right poer on both sides
    # of subwindow
    left = 0
    right = 0

    # ialize the frequency
    freq = 0

    # result and Length of string
    result = 0
    Len = len(s)

    # initialize the left poer
    while (s[left] != c and left < Len):
        left += 1
        leftCount += 1

    # initialize the right poer
    right = left + 1
    while (freq != (k - 1) and (right - 1) < Len):
        if (s[right] == c):
            freq += 1
        right += 1

    # traverse all the window substrings
    while (left < Len and (right - 1) < Len):

        # counting the characters on leftSide
        # of subwindow
        while (s[left] != c and left < Len):
            left += 1
            leftCount += 1

        # counting the characters on rightSide of
        # subwindow
        while (right < Len and s[right] != c):
            if (s[right] == c):
                freq += 1
            right += 1
            rightCount += 1

        # Add the possible substrings on both
        # sides to result
        result = (result + (leftCount + 1) *
                  (rightCount + 1))

        # Setting the frequency for next
        # subwindow
        freq = k - 1

        # reset the left, right counters
        leftCount = 0
        rightCount = 0

        left += 1
        right += 1

    return result


t=int(input())
for _ in range(t):
    c,k=map(int, input().split())
    s = input()

    print(countSubString(s, c, k))