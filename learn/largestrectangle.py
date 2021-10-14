#!/bin/python3


# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    stack = []
    area =i = 0
    h.append(0)
    while i<len(h):
        if len(stack)==0 or h[stack[-1]]<h[i]:
            stack.append(i)
            i+=1
        else:
            top = stack.pop()
            if stack:
                x = i-stack[-1]-1
            else:
                x = i
            area = max(area,h[top]*x)
    return area
if __name__ == '__main__':

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)