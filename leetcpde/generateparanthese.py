def isBalanced(s):
    hashmap = {")":"("}
    stack = []
    for i in s:
        if i in hashmap:
            if len(stack)==0:
                return False
            top_element = stack.pop()
            if hashmap[i]!=top_element:
                return False
        else:
            stack.append(i)
    return True if len(stack)==0 else False
s = []
def permutation(x,y,n):
    if y==n-1:
        if isBalanced(x):
            print(x)
    else:
        for i in range(y,n):
            x[i],x[y] = x[y],x[i]
            permutation(x,y+1,n)
            x[i],x[y] = x[y],x[i]

permutation(['(','(',')',')'],0,4)
print(s)

