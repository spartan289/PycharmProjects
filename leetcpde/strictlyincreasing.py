def canBeIncreasing(nums: list[int]) -> bool:
    count = 0
    index = -1
    n = len(nums)
    for i in range(1,n):
        if nums[i-1]>=nums[i]:
            count+=1
            index=i
    if (count > 1):
        return False;
    if (count == 0):
        return True;
    if (index == n - 1 or index == 1):
        return True;
    if (nums[index - 1] < nums[index + 1]):
        return True;
    if (nums[index - 2] < nums[index]):
        return True;

    return False;


def removealloccurence(string,part):
    stack = []
    n = len(string)
    m = len(part)
    for i in range(n):
        stack.append((string[i]))
        if len(stack)>=m:
            l = ""
            for j in range(m-1,-1,-1):
                if part[j]!=stack[-1]:
                    f=0
                    while f!=len(l):
                        stack.append(l[f])
                        f+=1
                    break
                else:
                    l = stack[-1]+l
                    stack.pop()
    x = ''
    for i in stack:
        x += i
    return x
print(removealloccurence("axxxxyyyyb","xy"))

